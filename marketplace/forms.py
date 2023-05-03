from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import SalesAd, ConversationMessage


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password'
    }))


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class NewAdForm(forms.ModelForm):
    """
    Form used to create new sales ads (sold field is not displayed)
    """
    class Meta:
        model = SalesAd
        fields = ('category', 'item_image', 'title', 'author', 'price', 'description', 'city')


class SalesAdForm(forms.ModelForm):
    """
    Form used to edit sales ads
    """
    class Meta:
        model = SalesAd
        fields = ('category', 'item_image', 'title', 'author', 'price', 'description', 'city', 'sold')


class ConversationMessageForm(forms.ModelForm):
    """
    A charfield to write a DM to a user
    """
    class Meta:
        model = ConversationMessage
        fields = ('content',)
        widgets = {
            'content': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Type your message here...',
            })
        }