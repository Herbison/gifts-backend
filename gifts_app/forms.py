from django import forms
from .models import Gift, Member

class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ['gift_adder', 'gift_receiver', 'item_name', 'links', 'exact_item', 'multiple', 'notes', 'date_to_remove', 'bought', 'visible_to']
        # Not using links, date_to_remove, or bought yet. Handle those on display?
        # field = '__all__' # Not sure if this handles foreignkey/many-to-many fields
        widgets = {
            'visible_to': forms.CheckboxSelectMultiple(),
        }