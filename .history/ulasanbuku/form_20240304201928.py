from django import forms
from .models import Ulasanbuku

class UlasanbukuForm(forms.ModelForm):
    class Meta:
        model = Ulasanbuku
        fields = ('Koleksiid', 'userid','bukuid')