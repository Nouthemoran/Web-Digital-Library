from django import forms
from .models import Kategoribuku

class KategoribukuForm(forms.ModelForm):
    class Meta:
        model = Kategoribuku
        fields = ('kategoriid', 'namakategori')