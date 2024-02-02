from django import forms
from .models import Gift

class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ['gift_receiver', 'item_name', 'exact_item', 'multiple', 'notes', 'date_to_remove', 'visible_to', 'links']
