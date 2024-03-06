
from django.shortcuts import render, redirect, get_object_or_404
from .models import 
from .form import Form
from django.forms import HiddenInput
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def _list(request):
    books = .objects.all()
    return render(request, 'list_/Admin.html', {'books': books})

def Peminjam__list(request):
    books = .objects.all()
    return render(request, 'list_/Peminjam.html', {'books': books})

def create_(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect(':read')
    else:
        form = Form()
    return render(request, 'form_/Admin.html', {'form': form})

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
