
from django.shortcuts import render, redirect, get_object_or_404
from .models import Koleksipribadi
from .form import KoleksipribadiForm
from django.forms import HiddenInput
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def Koleksipribadi_list(request):
    koleksis = Koleksipribadi.objects.all()
    return render(request, 'list_Koleksi/Admin.html', {'koleksis': koleksis})

def Peminjam_Koleksipribadi_list(request):
    koleksis = Koleksipribadi.objects.all()
    return render(request, 'list_Koleksi/Peminjam.html', {'koleksis': koleksis})

def create_Koleksipribadi(request):
    if request.method == 'POST':
        form = KoleksipribadiForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Koleksipribadi:read')
    else:
        form = KoleksipribadiForm()
    return render(request, 'form_Koleksipribadi/Admin.html', {'form': form})

def update_Koleksipribadi(request, Koleksipribadiid):
    koleksipribadi = get_object_or_404(Koleksipribadi, Koleksipribadiid=Koleksipribadiid)
    if request.method == 'POST':
        form = KoleksipribadiForm(request.POST, instance=koleksipribadi)
        if form.is_valid():
            form.save()
            return redirect('Koleksipribadi:read')
    else:
        form = KoleksipribadiForm(instance=koleksipribadi)
        form.fields['Koleksipribadiid'].widget = HiddenInput()

    return render(request, 'form_Koleksipribadi/Admin.html', {'form': form})

def delete_Koleksipribadi(request, Koleksipribadiid):
    Koleksipribadi = get_object_or_404(oleksipribadi, Koleksipribadiid=Koleksipribadiid)
    Koleksipribadi.delete()
    return redirect('Koleksipribadi:read')
