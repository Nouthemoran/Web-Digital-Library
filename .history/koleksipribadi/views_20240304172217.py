
from django.shortcuts import render, redirect, get_object_or_404
from .models import Koleksipribadu
from .form import KoleksipribaduForm
from django.forms import HiddenInput
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def Koleksipribadu_list(request):
    books = Koleksipribadu.objects.all()
    return render(request, 'list_Koleksipribadu/Admin.html', {'books': books})

def Peminjam_Koleksipribadu_list(request):
    books = Koleksipribadu.objects.all()
    return render(request, 'list_Koleksipribadu/Peminjam.html', {'books': books})

def create_Koleksipribadu(request):
    if request.method == 'POST':
        form = KoleksipribaduForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Koleksipribadu:read')
    else:
        form = KoleksipribaduForm()
    return render(request, 'form_Koleksipribadu/Admin.html', {'form': form})

def update_Koleksipribadu(request, Koleksipribaduid):
    Koleksipribadu = get_object_or_404(Koleksipribadu, Koleksipribaduid=Koleksipribaduid)
    if request.method == 'POST':
        form = KoleksipribaduForm(request.POST, instance=Koleksipribadu)
        if form.is_valid():
            form.save()
            return redirect('Koleksipribadu:read')
    else:
        form = KoleksipribaduForm(instance=Koleksipribadu)
        form.fields['Koleksipribaduid'].widget = HiddenInput()

    return render(request, 'form_Koleksipribadu/Admin.html', {'form': form})

def delete_Koleksipribadu(request, Koleksipribaduid):
    Koleksipribadu = get_object_or_404(Koleksipribadu, Koleksipribaduid=Koleksipribaduid)
    Koleksipribadu.delete()
    return redirect('Koleksipribadu:read')
