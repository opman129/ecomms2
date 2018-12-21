from django import forms

from .models import Cinema

class CinemaForm(forms.ModelForm):
    title       = forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
    content = forms.CharField(
                        widget=forms.Textarea(attrs={"placeholder": "Your content"})
    )
    image   = forms.FileField()
    #email       = forms.EmailField()
    class Meta:
        model   = Cinema
        fields  = [
            'title',
            'content',
            'image',
            'draft',
            'published'
]