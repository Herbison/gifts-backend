from django import forms
from .models import Gift, Member

class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ['gift_receiver', 'item_name', 'exact_item', 'multiple', 'notes', 'date_to_remove', 'visible_to', 'links']

    def __init__(self, *args, **kwargs):
        # Extract view_type from kwargs and remove it before calling super()
        view_type = kwargs.pop('view_type', 'other')
        super().__init__(*args, **kwargs)

        # For the "other" view, set visibility to all by default and hide the field
        if view_type == 'other':
            self.fields['visible_to'].initial = Member.objects.all()
            self.fields['visible_to'].widget = forms.MultipleHiddenInput()
        else:
            # For the "self" view, provide a widget to choose visibility
            self.fields['visible_to'].queryset = Member.objects.exclude(id=kwargs['initial']['gift_receiver'])
            self.fields['visible_to'].widget = forms.CheckboxSelectMultiple()

        # Handle the 'links' ManyToManyField
        self.fields['links'].widget = forms.TextInput()  # Or any other widget as per your need

    def save(self, commit=True):
        # Save the instance normally first
        instance = super().save(commit=False)

        # If commit is True, save the instance and m2m data
        if commit:
            instance.save()
            self.save_m2m()

            # For "other" view type, set visibility to all members after saving
            if 'visible_to' not in self.cleaned_data or self.cleaned_data['visible_to'] is None:
                instance.visible_to.set(Member.objects.all())

        return instance
