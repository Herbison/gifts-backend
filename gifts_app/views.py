from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import GiftSerializer
from django.contrib.auth.models import User

@api_view(["POST"])
def create_gift(request):
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