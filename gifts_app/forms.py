from django import forms
from .models import Gift

class AddOtherForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = [
            'gift_receiver', 'item_name', 'exact_item',
            'multiple', 'notes', 'bought', 'date_to_remove',
            'visible_to'
        ]
        widgets = {
            'gift_receiver': forms.Select(),
            'item_name': forms.TextInput(attrs={'maxlength': 100}),
            'exact_item': forms.CheckboxInput(),
            'multiple': forms.CheckboxInput(),
            'notes': forms.Textarea(attrs={'maxlength': 1000}),
            'bought': forms.CheckboxInput(),
            # Only allow date_to_remove is bought is True
            'date_to_remove': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
            # 'visible_to' 
                # Add multiple-select widget
        }

class AddSelfForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = [
            'item_name', 'exact_item', 'multiple', 'notes', 'date_to_remove', 'visible_to'
        ]
        widgets = {
            'item_name': forms.TextInput(attrs={'maxlength': 100}),
            'exact_item': forms.CheckboxInput(),
            'multiple': forms.CheckboxInput(),
            'notes': forms.Textarea(attrs={'maxlength': 1000}),
            'date_to_remove': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
            # 'visible_to' 
                # Add multiple-select widget
        }