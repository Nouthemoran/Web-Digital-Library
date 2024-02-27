# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .models import User

class RegistrationForm(UserCreationForm):
    ROLES = (
        ('admin', 'Admin'),
        ('petugas', 'Petugas'),
        ('peminjam', 'Peminjam'),
    )
    role = forms.ChoiceField(choices=ROLES)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','namalengkap', 'alamat', 'role')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            role = self.cleaned_data.get('role')
            group = Group.objects.get(name=role)
            user.groups.add(group)
        return user