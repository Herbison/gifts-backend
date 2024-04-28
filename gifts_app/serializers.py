from rest_framework import serializers
from .models import Gift, Link, Member

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["name", "url"]

class GiftSerializer(serializers.ModelSerializer):
    links = LinkSerializer(many=True, read_only=True)
    class Meta:
        model = Gift
        fields = ["gift_id", "gift_receiver", "item_name", "exact_item", "multiple", "notes", "date_to_remove", "bought", "visible_to", "added_by", "links"]

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ["member_id", "member_name", "show_bought"]