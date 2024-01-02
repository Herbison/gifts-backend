from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import GiftSerializer
from django.contrib.auth.models import User
from .forms import AddOtherForm, AddSelfForm
from django.http import JsonResponse



@api_view(["POST"])
def create_gift_self(request):
    form = AddOtherForm(request.POST)
    if form.is_valid():
        gift_id = form.cleaned_data.get("gift_id")
        #Add other fields
    return JsonResponse(
        {
            "message": "Gift added successfully",
        }
    )
    pass

@api_view(["POST"])
def create_gift_other(request):
    form = AddSelfForm(request.POST)
    pass

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