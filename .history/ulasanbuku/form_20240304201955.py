from django import forms
from .models import Ulasanbuku

class UlasanbukuForm(forms.ModelForm):
    class Meta:
        model = Ulasanbuku
        fields = ('Ulasanid', 'userid','bukuid', 'u')