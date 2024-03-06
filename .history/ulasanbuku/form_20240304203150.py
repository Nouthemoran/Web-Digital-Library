from django import forms
from .models import Ulasanbuku

class UlasanbukuForm(forms.ModelForm):
    class Meta:
        model = Ulasanbuku
        fields = ('ulasanid', 'userid','bukuid', 'ulasan', 'rat')