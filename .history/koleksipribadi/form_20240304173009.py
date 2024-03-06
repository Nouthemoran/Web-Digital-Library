from django import forms
from .models import 

class Form(forms.ModelForm):
    class Meta:
        model = 
        fields = ('id', 'judul','kategoriid', 'penulis', 'penerbit','tahunterbit')