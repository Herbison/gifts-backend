# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework import status
# from .serializers import GiftSerializer
# May need these later, but not actively using them now

from rest_framework.decorators import api_view
from .forms import GiftForm
from django.http import JsonResponse
from .models import Gift, Member
from django.db.models import Prefetch




@api_view(["POST"])
def create_gift(request):
    form = GiftForm(request.POST)
    if form.is_valid():
        gift_id = form.cleaned_data.get("gift_id")

        # Add gift to DB

        return JsonResponse(
            {
                "message": "Gift added successfully",
            }
        )
    else:
        return JsonResponse(
            {
                "message": "Form is not valid",
            }
        )

@api_view(["GET"])
def get_all_members(request):
    members = Member.objects.all()
    member_list = members.values(
        "member_id", # Primary Key
        "member_name",
        "show_bought",    
    )
    return JsonResponse({"members": list(member_list)})

@api_view(["GET"])
def get_all_gifts_self(request):
    member_id = request.query_params.get('member_id')
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
                'date_to_remove': gift.date_to_remove,
                'bought': gift.bought,
                'visible_to': list(gift.visible_to.values_list('member_name', flat=True))
            }
            for gift in self_gifts
        ]
        return JsonResponse({'gifts': gift_list})
    else:
        return JsonResponse({'error': 'No member_id provided'}, status=400)

def get_all_gifts_other(request):
    # member_id = request.query_params.get('member_id')
    pass

@api_view(["PUT"])
def update_gift(request):
    pass

@api_view(["DELETE"])
def remove_gift(request):
    pass