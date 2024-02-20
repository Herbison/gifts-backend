from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import GiftSerializer
from .forms import GiftForm
from django.http import JsonResponse
from .models import Gift, Member



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
def get_all_gifts(request):
    gifts = Gift.objects.all()
    gift_list = gifts.values(
        "gift_id", # Primary Key
        "gift_adder",
        "gift_receiver",
        "item_name",
        "exact_item",
        "multiple",
        "notes",
        "date_to_remove",
        "bought",
        "visible_to",
    )
    return JsonResponse({"gifts": list(gift_list)})

@api_view(["PUT"])
def update_gift(request):
    pass

@api_view(["DELETE"])
def remove_gift(request):
    pass