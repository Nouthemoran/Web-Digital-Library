
from django.shortcuts import render, redirect, get_object_or_404
from .models import d
from buku.models import Buku
from .form import dForm
from django.forms import HiddenInput
from django.http import HttpResponseRedirect

def admin_d_list(request):
    pinjams = d.objects.all()
    return render(request, 'list_d/Admin.html', {'pinjams': pinjams})

def d_list(request):
    pinjams = d.objects.all()
    return render(request, 'list_d/Peminjam.html', {'pinjams': pinjams})

def create_d(request):
    if request.method == 'POST':
        form = dForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('d:read')
    else:
        form = dForm()
    return render(request, 'form_d/Peminjam.html', {'form': form})

def update_d(request, did):
    d = get_object_or_404(d, did=did)
    if request.method == 'POST':
        form = dForm(request.POST, instance=d)
        if form.is_valid():
            form.save()
            return redirect('d:read')
    else:
        form = dForm(instance=d)
        form.fields['did'].widget = HiddenInput()

    return render(request, 'form_d/Admin.html', {'form': form})

def delete_d(request, did):
    d = get_object_or_404(d, did=did)
    d.delete()
    return redirect('d:read')
