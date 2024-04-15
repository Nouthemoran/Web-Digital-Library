
from django.shortcuts import render, redirect, get_object_or_404
from .models import Koleksipribadi
from .form import KoleksipribadiForm
from django.forms import HiddenInput
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from buku.models import Buku

def Koleksipribadi_list(request):
    koleksis = Koleksipribadi.objects.all()
    return render(request, 'list_Koleksi/Peminjam.html', {'koleksis': koleksis})

def create_Koleksipribadi(request):
    bukuid = get_object_or_404(Buku, bukuid=bukuid)
    if request.method == 'POST':
        form = KoleksipribadiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Koleksipribadi:read')
    else:
        form = KoleksipribadiForm(instance=bukuid)
    return render(request, 'form_Koleksi/Admin.html', {'form': form})

def update_Koleksipribadi(request, Koleksiid):
    koleksipribadi = get_object_or_404(Koleksipribadi, Koleksiid=Koleksiid)
    if request.method == 'POST':
        form = KoleksipribadiForm(request.POST, instance=koleksipribadi)
        if form.is_valid():
            form.save()
            return redirect('Koleksipribadi:read')
    else:
        form = KoleksipribadiForm(instance=koleksipribadi)
        form.fields['Koleksiid'].widget = HiddenInput()

    return render(request, 'form_Koleksi/Admin.html', {'form': form})

def delete_Koleksipribadi(request, Koleksiid):
    koleksipribadi = get_object_or_404(Koleksipribadi, Koleksiid=Koleksiid)
    koleksipribadi.delete()
    return redirect('Koleksipribadi:read')
