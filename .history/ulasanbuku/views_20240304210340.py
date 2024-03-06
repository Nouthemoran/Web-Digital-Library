
from django.shortcuts import render, redirect, get_object_or_404
from .models import Ulasanbuku
from buku.models import Buku
from .form import UlasanbukuForm
from django.forms import HiddenInput
from django.http import HttpResponseRedirect

def admin_Ulasanbuku_list(request):
    pinjams = Ulasanbuku.objects.all()
    return render(request, 'list_Ulasan/Admin.html', {'pinjams': pinjams})

def Ulasanbuku_list(request):
    pinjams = Ulasanbuku.objects.all()
    return render(request, 'list_Ulasan/Peminjam.html', {'pinjams': pinjams})

def create_Ulasanbuku(request):
    if request.method == 'POST':
        form = UlasanbukuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Ulasanbuku:read')
    else:
        form = UlasanbukuForm()
    return render(request, 'form_Ulasan/Peminjam.html', {'form': form})

def update_Ulasanbuku(request, Ulasanbukuid):
    ulasanbuku = get_object_or_404(Ulasanbuku, Ulasanbukuid=Ulasanbukuid)
    if request.method == 'POST':
        form = UlasanbukuForm(request.POST, instance=ulasanbuku)
        if form.is_valid():
            form.save()
            return redirect('Ulasanbuku:read')
    else:
        form = UlasanbukuForm(instance=ulasanbuku)
        form.fields['Ulasanbukuid'].widget = HiddenInput()

    return render(request, 'form_Ulasan/Admin.html', {'form': form})

def delete_Ulasanbuku(request, Ulasanbukuid):
    ulasanbuku = get_object_or_404(Ulasanbuku, Ulasanbukuid=Ulasanbukuid)
    ulasanbuku.delete()
    return redirect('Ulasanbuku:read')
