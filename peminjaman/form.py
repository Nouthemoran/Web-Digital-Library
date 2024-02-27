from django import forms
from .models import Peminjaman

class PeminjamanForm(forms.ModelForm):
    class Meta:
        model = Peminjaman
        fields = ('peminjamanid', 'userid', 'bukuid', 'tanggalpeminjaman', 'tanggalpengembalian', 'statuspeminjaman')
        widgets = {
            'tanggalpeminjaman': forms.DateInput(attrs={'type': 'date'}),
            'tanggalpengembalian': forms.DateInput(attrs={'type': 'date'}),
        }