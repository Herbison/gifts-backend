# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import GiftSerializer
# May need these later, but not actively using them now

import json
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework import status
# from .forms import GiftForm
from django.http import JsonResponse
from .models import Gift, Member, Link
from django.db.models import Prefetch

def redirect_to_admin(request):
    return redirect('/admin/')

def health_check(request):
    return JsonResponse({"status": "ok"}, status=200)

@api_view(["GET"])
def get_all_members(request):
    members = Member.objects.all()
    member_list = members.values(
        "member_id", # Primary Key
        "member_name",    
    )
    return JsonResponse({"members": list(member_list)})

# Combining add_gift and edit_gift into manage_gift
@api_view(["POST"])
def add_gift(request):

    gift_data = {
        'gift_adder_id': request.data.get('giftAdder'),
        'gift_receiver_id': request.data.get('giftReceiver'),
        'item_name': request.data.get('itemName'),
        'exact_item': request.data.get('exactItem') == 'true',
        'multiple': request.data.get('multiple') == 'true',
        'notes': request.data.get('notes'),
        'other_notes': request.data.get('otherNotes'),
        'bought': request.data.get('boughtStatus'),
    }

    gift = Gift(**gift_data)
    gift.save()

    ## Handling visibility
    # Parses the JSON string for visibility back into a Python list
    visibility_ids = json.loads(request.data.get('visibility', '[]'))

    # Set the many-to-many relationship
    for member_id in visibility_ids:
        gift.visible_to.add(Member.objects.get(pk=member_id))

    ##Handling link(s)
    # Add default for link_name of "Link" if not provided
    link_url = request.POST.get('linkURL')
    link_name = request.POST.get('linkName')
    if link_url and link_name:
        Link.objects.create(gift=gift, url=link_url, name=link_name)
    
    return JsonResponse({
        'message': 'Gift added successfully',
        'gift_id': gift.gift_id
    }, status=201)

@api_view(["PUT"])
def edit_gift_by_id(request, gift_id):
    gift = Gift.objects.get(pk=gift_id)

    gift.item_name = request.data.get('itemName')
    gift.exact_item = request.data.get('exactItem') == 'true'
    gift.multiple = request.data.get('multiple') == 'true'
    gift.notes = request.data.get('notes')
    gift.other_notes = request.data.get('otherNotes')
    gift.bought = request.data.get('boughtStatus')
    gift.save()

    ## Handling visibility
    # Parses the JSON string for visibility back into a Python list
    visibility_ids = json.loads(request.data.get('visibility', '[]'))

    # Set the many-to-many relationship. Clear the existing visibility list first.
    gift.visible_to.clear()
    for member_id in visibility_ids:
        gift.visible_to.add(Member.objects.get(pk=member_id))

    ##Handling link(s)
    # Add default for link_name of "Link" if not provided
    link_url = request.POST.get('linkURL')
    link_name = request.POST.get('linkName')
    if link_url and link_name:
        Link.objects.create(gift=gift, url=link_url, name=link_name)

    return JsonResponse({
        'message': 'Gift updated successfully',
        'gift_id': gift.gift_id
    }, status=200)

@api_view(["DELETE"])
def delete_gift_by_id(request, gift_id):
    gift = Gift.objects.get(pk=gift_id)
    gift.delete()
    return JsonResponse({
        'message': 'Gift deleted successfully',
        'gift_id': gift.gift_id
    }, status=200)

@api_view(["GET"])
def get_gifts_self(request, member_id):
    if member_id is not None:
        member = Member.objects.get(pk=member_id)
        # Optimizes the query for the 'visible_to' relationship
        visible_gifts = member.visible_gifts.prefetch_related(
            Prefetch('visible_to', queryset=Member.objects.only('member_name'))
        )
        self_gifts = visible_gifts.filter(gift_receiver=member)

        # Builds a list of gifts with custom structure including 'visible_to' member names
        gift_list = [
            {
                'gift_id': gift.gift_id,
                'gift_adder': gift.gift_adder.member_name,
                'gift_receiver': gift.gift_receiver.member_name,
                'item_name': gift.item_name,
                'exact_item': gift.exact_item,
                'multiple': gift.multiple,
                'notes': gift.notes,
                'visible_to': list(gift.visible_to.values_list('member_name', flat=True)),
                'links': list(gift.links.values('name', 'url'))
            }
            for gift in self_gifts
        ]
        return JsonResponse({'gifts': gift_list})
    else:
        return JsonResponse({'error': 'No member_id provided'}, status=400)

@api_view(["GET"])
def get_gifts_other(request, member_id):
    if member_id is not None:
        self_member = Member.objects.get(pk=member_id)
        # Get gifts where self_member is in visible_to but is not the receiver
        gifts = Gift.objects.filter(
            visible_to=self_member
        ).exclude(
            gift_receiver=self_member
        )

        # Serialize the gifts data
        gifts_list = [
            {
                'gift_id': gift.gift_id,
                'gift_adder': gift.gift_adder.member_name,
                'gift_receiver': gift.gift_receiver.member_name,
                'item_name': gift.item_name,
                'exact_item': gift.exact_item,
                'multiple': gift.multiple,
                'notes': gift.notes,
                'other_notes': gift.other_notes,
                'links': list(gift.links.values('name', 'url')),
                'bought': gift.bought
            }
            for gift in gifts
        ]

        return JsonResponse({'gifts': gifts_list})
    else:
        return JsonResponse({'error': 'No self_member_id provided'}, status=400)
    
@api_view(["GET"])
def get_gift_by_id(request, gift_id):
    gift = Gift.objects.get(pk=gift_id)
    gift_data = {
        'gift_id': gift.gift_id,
        'gift_adder': gift.gift_adder.member_name,
        'gift_receiver': gift.gift_receiver.member_name,
        'item_name': gift.item_name,
        'exact_item': gift.exact_item,
        'multiple': gift.multiple,
        'notes': gift.notes,
        'other_notes': gift.other_notes,
        'visible_to': list(gift.visible_to.values_list('member_id', flat=True)),
        'links': list(gift.links.values('name', 'url')),
        'bought': gift.bought
    }
    return JsonResponse({'gift': gift_data})