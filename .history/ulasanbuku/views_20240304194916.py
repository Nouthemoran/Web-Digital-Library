
from django.shortcuts import render, redirect, get_object_or_404
from .models import d\
from buku.models import Buku
from .form import d\Form
from django.forms import HiddenInput
from django.http import HttpResponseRedirect

def admin_d\_list(request):
    pinjams = d\.objects.all()
    return render(request, 'list_d\/Admin.html', {'pinjams': pinjams})

def d\_list(request):
    pinjams = d\.objects.all()
    return render(request, 'list_d\/Peminjam.html', {'pinjams': pinjams})

def create_d\(request):
    if request.method == 'POST':
        form = d\Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('d\:read')
    else:
        form = d\Form()
    return render(request, 'form_d\/Peminjam.html', {'form': form})

def update_d\(request, d\id):
    d\ = get_object_or_404(d\, d\id=d\id)
    if request.method == 'POST':
        form = d\Form(request.POST, instance=d\)
        if form.is_valid():
            form.save()
            return redirect('d\:read')
    else:
        form = d\Form(instance=d\)
        form.fields['d\id'].widget = HiddenInput()

    return render(request, 'form_d\/Admin.html', {'form': form})

def delete_d\(request, d\id):
    d\ = get_object_or_404(d\, d\id=d\id)
    d\.delete()
    return redirect('d\:read')
