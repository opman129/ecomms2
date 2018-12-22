from django import forms

from .models import Project

class ProjectForm(forms.ModelForm):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
    description = forms.CharField(
                        widget=forms.Textarea(attrs={"placeholder": "Your description"})
    )
    price       = forms.DecimalField(initial=200.00, max_value=400.00, decimal_places=7)
    email       = forms.EmailField()
    class Meta:
        model   = Project
        fields  = [
            'title',
            'description',
            'price'
]


    #def clean_title(self, **args, **kwargs):
    #    title = self.cleaned_data.get("title")
    #    if not "ope" in title:
     #       raise forms.ValidationError("Invalid title")
       # return title

#    def clean_email(self, **args, **kwargs):
#        email = self.cleaned_data.get("email")
#        if not email.endswith("edu"):
#            raise forms.ValidationError("Invalid email")
#        return email
            
        



class RawProjectForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Title"}))
    description = forms.CharField(
                        widget=forms.Textarea(attrs={"placeholder": "Your description"})
    )
    price       = forms.DecimalField(initial=200.00)
