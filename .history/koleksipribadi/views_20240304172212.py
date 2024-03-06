
from django.shortcuts import render, redirect, get_object_or_404
from .models import Koleksi
from .form import KoleksiForm
from django.forms import HiddenInput
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def Koleksi_list(request):
    books = Koleksi.objects.all()
    return render(request, 'list_Koleksi/Admin.html', {'books': books})

def Peminjam_Koleksi_list(request):
    books = Koleksi.objects.all()
    return render(request, 'list_Koleksi/Peminjam.html', {'books': books})

def create_Koleksi(request):
    if request.method == 'POST':
        form = KoleksiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Koleksi:read')
    else:
        form = KoleksiForm()
    return render(request, 'form_Koleksi/Admin.html', {'form': form})

def update_Koleksi(request, Koleksiid):
    Koleksi = get_object_or_404(Koleksi, Koleksiid=Koleksiid)
    if request.method == 'POST':
        form = KoleksiForm(request.POST, instance=Koleksi)
        if form.is_valid():
            form.save()
            return redirect('Koleksi:read')
    else:
        form = KoleksiForm(instance=Koleksi)
        form.fields['Koleksiid'].widget = HiddenInput()

    return render(request, 'form_Koleksi/Admin.html', {'form': form})

def delete_Koleksi(request, Koleksiid):
    Koleksi = get_object_or_404(Koleksi, Koleksiid=Koleksiid)
    Koleksi.delete()
    return redirect('Koleksi:read')
