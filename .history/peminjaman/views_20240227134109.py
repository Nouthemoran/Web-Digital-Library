
from django.shortcuts import render, redirect, get_object_or_404
from .models import Peminjaman
from buku.models import Buku
from .form import PeminjamanForm
from django.forms import HiddenInput
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def admin_peminjaman_list(request):
    pinjams = Peminjaman.objects.all()
    return render(request, 'list/Admin_list.html', {'pinjams': pinjams})

def Peminjaman_list(request):
    pinjams = Peminjaman.objects.all()
    return render(request, 'list_Peminjaman/Peminjam_list.html', {'pinjams': pinjams})

def create_Peminjaman(request, bukuid):
    buku = get_object_or_404(Buku, bukuid=bukuid)
    if request.method == 'POST':
        form = PeminjamanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Peminjaman:read')
    else:
        form = PeminjamanForm(instance=buku)
    return render(request, 'form_Peminjaman/Peminjam_form.html', {'form': form})

def update_Peminjaman(request, peminjamanid):
    Peminjaman = get_object_or_404(Peminjaman, peminjamanid=peminjamanid)
    if request.method == 'POST':
        form = PeminjamanForm(request.POST, instance=Peminjaman)
        if form.is_valid():
            form.save()
            return redirect('Peminjaman:read')
    else:
        form = PeminjamanForm(instance=Peminjaman)
        form.fields['peminjamanid'].widget = HiddenInput()

    return render(request, 'form_Peminjaman/Admin_form.html', {'form': form})

def delete_Peminjaman(request, peminjamanid):
    Peminjaman = get_object_or_404(Peminjaman, peminjamanid=peminjamanid)
    Peminjaman.delete()
    return redirect('Peminjaman:read')
