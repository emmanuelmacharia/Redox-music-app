"""
Definition of forms.
"""


from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))
class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model=User
        fields=['username', 'email', 'password']
