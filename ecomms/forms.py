from django import forms

from .models import Message

class MessageForm(forms.ModelForm):
    Name       = forms.CharField(label='Name', widget=forms.TextInput(attrs={"placeholder": "Your Name"}))
    Email       = forms.EmailField(widget=forms.Textarea(attrs={"placeholder": "Your Email"}))
    Department = forms.CharField()
    Message = forms.TextField(
                        widget=forms.Textarea(attrs={"placeholder": "Your message"})
    )
    class Meta:
        model   = Message
        fields  = [
            'Name',
            'Email',
            'Department',
            'Message',
]