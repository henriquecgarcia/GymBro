from django import forms
from django.contrib.auth.models import User
from .models import GymUser

class GymUserForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    email = forms.EmailField(required=True)

    class Meta:
        model = GymUser
        fields = ['nome', 'idade', 'genero', 'academia', 'objetivo']

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password'],
            email=self.cleaned_data['email']
        )
        gym_user = super().save(commit=False)
        gym_user.user = user
        if commit:
            gym_user.save()
        return gym_user
