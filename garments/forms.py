from django import forms
class contactform(forms.Form):
    contact_name=forms.CharField(label='Enter your name',required=True)
    contact_email=forms.EmailField(label='Enter your email', required=True)
    content=forms.CharField(label='your Message',required=True ,widget=forms.Textarea)
    