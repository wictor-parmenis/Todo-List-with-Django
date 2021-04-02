from django import forms


class NewList(forms.Form):
    name = forms.CharField(label='Name', max_length=300)
    status = forms.BooleanField(required=False)