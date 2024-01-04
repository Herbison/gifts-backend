from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import GiftSerializer
from django.contrib.auth.models import User
from .forms import AddOtherForm, AddSelfForm
from django.http import JsonResponse



@api_view(["POST"])
def create_gift_other(request):
    form = AddOtherForm(request.POST)
    if form.is_valid():
        gift_id = form.cleaned_data.get("gift_id")
        gift_receiver = form.cleaned_data.get("gift_receiver")
        item_name = form.cleaned_data.get("item_name")
        exact_item = form.cleaned_data.get("exact_item")
        multiple = form.cleaned_data.get("multiple")
        notes = form.cleaned_data.get("notes")
        date_to_remove = form.cleaned_data.get("date_to_remove")
        bought = form.cleaned_data.get("bought")
        visible_to = form.cleaned_data.get("visible_to")
        added_by = request.user  # Adds the currently logged-in user

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

@api_view(["POST"])
def create_gift_self(request):
    form = AddSelfForm(request.POST)
    if form.is_valid():
        gift_id = form.cleaned_data.get("gift_id")
        #Add other fields
    return JsonResponse(
        {
            "message": "Gift added successfully",
        }
    )

@api_view(["GET"])
def get_self_view(request):
    pass

@api_view(["GET"])
def get_other_view(request):
    pass

@api_view(["PUT"])
def update_gift(request):
    pass

@api_view(["DELETES"])
def remove_gift(request):
    pass