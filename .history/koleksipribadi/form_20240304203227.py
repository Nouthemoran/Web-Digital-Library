from django import forms
from .models import Koleksipribadi

class KoleksipribadiForm(forms.ModelForm):
    class Meta:
        model = Koleksipribadi
        fields = ('koleksiid', 'userid','bukuid')