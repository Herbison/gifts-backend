from rest_framework import serializers
from .models import Gift, Link
from django.contrib.auth.models import User

class GiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gift
        fields = ["gift_id", "gift_receiver", "item_name", "exact_item", "multiple", "notes", "date_to_remove", "bought", "visible_to", "added_by"]

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["gift", "url"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']