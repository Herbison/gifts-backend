from django import forms
from .models import Gift, Member

class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ['gift_adder', 'gift_receiver', 'item_name', 'exact_item', 'multiple', 'notes', 'visible_to']
        widgets = {
            'visible_to': forms.CheckboxSelectMultiple(),
        }
        # Only fields I want to show. How do I handle visibility, which is only visible to selfMember?


class GiftForm(forms.Form):
    gift_adder = forms.ModelChoiceField(queryset=Member.objects.all(), empty_label="Select Adder", required=True)
    gift_receiver = forms.ModelChoiceField(queryset=Member.objects.all(), empty_label="Select Receiver", required=True)
    item_name = forms.CharField(max_length=100, required=True)
    # links = forms.CharField(widget=forms.Textarea, required=False)
        # Adding later
    exact_item = forms.BooleanField(required=False)
    multiple = forms.BooleanField(required=False)
    notes = forms.CharField(widget=forms.Textarea, required=False)
    visible_to = forms.ModelMultipleChoiceField(queryset=Member.objects.all(), required=False)
