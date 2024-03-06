
from django.shortcuts import render, redirect, get_object_or_404
from .models import 
from buku.models import Buku
from .form import Form
from django.forms import HiddenInput
from django.http import HttpResponseRedirect

def admin__list(request):
    pinjams = .objects.all()
    return render(request, 'list_/Admin.html', {'pinjams': pinjams})

def _list(request):
    pinjams = .objects.all()
    return render(request, 'list_/Peminjam.html', {'pinjams': pinjams})

def create_(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(':read')
    else:
        form = Form()
    return render(request, 'form_/Peminjam.html', {'form': form})

def update_(request, id):
     = get_object_or_404(, id=id)
    if request.method == 'POST':
        form = Form(request.POST, instance=)
        if form.is_valid():
            form.save()
            return redirect(':read')
    else:
        form = Form(instance=)
        form.fields['id'].widget = HiddenInput()

    return render(request, 'form_/Admin.html', {'form': form})

def delete_(request, id):
     = get_object_or_404(, id=id)
    .delete()
    return redirect(':read')
