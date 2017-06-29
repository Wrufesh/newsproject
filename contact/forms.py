from django import forms

from newsproject.utils.forms import BootstrapModelForm
from .models import Message


class ContactForm(BootstrapModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}), required=True)
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message', 'rows': 2}),
                              required=True)

    class Meta:
        model = Message
        fields = ['name', 'email', 'message']
