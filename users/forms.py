from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from instruments.models import Instrument

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    bio = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3}),
        required=False
    )
    instruments = forms.ModelMultipleChoiceField(
        queryset=Instrument.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    profile_picture = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'bio', 'instruments', 'profile_picture']