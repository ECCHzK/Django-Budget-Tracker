from datetime import datetime
from email.policy import default
from socket import fromshare
from django import forms

class AddToBudget(forms.Form):
    date = forms.DateField(required=False, widget=forms.TextInput(attrs={'placeholder':'Date'}))
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder':'Name'}))
    amount = forms.DecimalField(min_value=0, decimal_places=2, max_digits=99, widget=forms.TextInput(attrs={'placeholder':'Amount'}))
    iscost = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class':'btn-check', 'role':'switch'}), initial=False, required=False)