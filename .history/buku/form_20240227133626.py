from django import forms
from .models import Buku

class BukuForm(forms.ModelForm):
    class Meta:
        model = Buku
        fields = ('bukuid', 'judul','' 'penulis', 'penerbit','tahunterbit')