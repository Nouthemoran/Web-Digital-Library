
from django.shortcuts import render, redirect, get_object_or_404
from .models import Kategoribuku
from buku.models import Buku
from .form import KategoribukuForm
from django.forms import HiddenInput
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def Kategoribuku_list(request):
    kategoris = Kategoribuku.objects.all()
    return render(request, 'list_kategori/Admin.html', {'kategoris': kategoris})

def Peminjam_Kategoribuku_list(request):
    kategoris = Kategoribuku.objects.all()
    return render(request, 'list_kategori/Peminjam.html', {'kategoris': kategoris})

def lihat_buku_per_kategori(request, kategoriid):
    kategoris = Kategoribuku.objects.get(pk=kategoriid)
    bukus = Buku.objects.filter(kategoriid=kategoriid)
    return render(request, 'list_buku/Peminjam.html', {'kategori': kategoris, 'bukus': bukus})

def create_Kategoribuku(request):
    if request.method == 'POST':
        form = KategoribukuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Kategoribuku:read')
    else:
        form = KategoribukuForm()
    return render(request, 'form_kategori/Admin.html', {'form': form})

def update_Kategoribuku(request, kategoriid):
    kategoribuku = get_object_or_404(Kategoribuku, kategoriid=kategoriid)
    if request.method == 'POST':
        form = KategoribukuForm(request.POST, instance=kategoribuku)
        if form.is_valid():
            form.save()
            return redirect('Kategoribuku:read')
    else:
        form = KategoribukuForm(instance=kategoribuku)
        form.fields['kategoriid'].widget = HiddenInput()

    return render(request, 'form_kategori/Admin.html', {'form': form})

def delete_Kategoribuku(request, kategoriid):
    kategoribuku = get_object_or_404(Kategoribuku, kategoriid=kategoriid)
    kategoribuku.delete()
    return redirect('Kategoribuku:read')
