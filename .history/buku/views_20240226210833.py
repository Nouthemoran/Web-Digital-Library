
from django.shortcuts import render, redirect, get_object_or_404
from .models import Buku
from .form import BukuForm
from django.forms import HiddenInput
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def Buku_list(request):
    books = Buku.objects.all()
    return render(request, 'list/Admin.html', {'books': books})

def Peminjam_buku_list(request):
    books = Buku.objects.all()
    return render(request, 'list/Peminjam.html', {'books': books})

def create_Buku(request):
    if request.method == 'POST':
        form = BukuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Buku:read')
    else:
        form = BukuForm()
    return render(request, 'form/Admin.html', {'form': form})

def update_Buku(request, bukuid):
    buku = get_object_or_404(Buku, bukuid=bukuid)
    if request.method == 'POST':
        form = BukuForm(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            return redirect('Buku:read')
    else:
        form = BukuForm(instance=buku)
        form.fields['bukuid'].widget = HiddenInput()

    return render(request, 'form/Admin_form.html', {'form': form})

def delete_Buku(request, bukuid):
    buku = get_object_or_404(Buku, bukuid=bukuid)
    buku.delete()
    return redirect('Buku:read')
