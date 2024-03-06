
from django.shortcuts import render, redirect, get_object_or_404
from .models import Ulasan
from buku.models import Buku
from .form import UlasanForm
from django.forms import HiddenInput
from django.http import HttpResponseRedirect

def admin_Ulasan_list(request):
    pinjams = Ulasan.objects.all()
    return render(request, 'list_Ulasan/Admin.html', {'pinjams': pinjams})

def Ulasan_list(request):
    pinjams = Ulasan.objects.all()
    return render(request, 'list_Ulasan/Peminjam.html', {'pinjams': pinjams})

def create_Ulasan(request):
    if request.method == 'POST':
        form = UlasanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Ulasan:read')
    else:
        form = UlasanForm()
    return render(request, 'form_Ulasan/Peminjam.html', {'form': form})

def update_Ulasan(request, Ulasanid):
    Ulasan = get_object_or_404(Ulasan, Ulasanid=Ulasanid)
    if request.method == 'POST':
        form = UlasanForm(request.POST, instance=Ulasan)
        if form.is_valid():
            form.save()
            return redirect('Ulasan:read')
    else:
        form = UlasanForm(instance=Ulasan)
        form.fields['Ulasanid'].widget = HiddenInput()

    return render(request, 'form_Ulasan/Admin.html', {'form': form})

def delete_Ulasan(request, Ulasanid):
    Ulasan = get_object_or_404(Ulasan, Ulasanid=Ulasanid)
    Ulasan.delete()
    return redirect('Ulasan:read')
