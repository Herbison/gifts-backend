from django import forms
from .models import Gift

class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ['gift_receiver', 'item_name', 'exact_item', 'multiple', 'notes', 'visible_to', 'links']
        # Only fields I want to show. How do I handle visibility, which is only visible to selfMember?
