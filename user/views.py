from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from .form import RegistrationForm
from .models import User
from django.contrib.auth.models import Group
from django.contrib.auth import logout
from buku.models import Buku
from kategoribuku.models import Kategoribuku

class CustomLoginView(LoginView):
    template_name = 'auth/login.html'  

    def get_success_url(self):
        user = self.request.user
        if user.is_authenticated:
            if user.groups.filter(name='petugas').exists():
                return reverse('User:petugas_dashboard')  # Ganti 'staff_dashboard' dengan nama URL untuk dashboard petugas
            elif user.groups.filter(name='peminjam').exists():
                return reverse('User:peminjam-read')  # Ganti 'borrower_dashboard' dengan nama URL untuk dashboard peminjam
            elif user.groups.filter(name='admin').exists():
                return reverse('User:admin_dashboard')  # Ganti 'admin_dashboard' dengan nama URL untuk dashboard administrator
    

@login_required
def admin_dashboard(request):
    total_books = Buku.objects.count()
    total_kategoris = Kategoribuku.objects.count()
    # Logika tampilan dashboard administrator
    return render(request, 'dashboard/admin_dashboard.html', {'total_books': total_books, 'total_kategoris': total_kategoris})

@login_required
def petugas_dashboard(request):
    total_books = Buku.objects.count()
    total_kategoris = Kategoribuku.objects.count()
    # Logika tampilan dashboard petugas
    return render(request, 'dashboard/petugas_dashboard.html', {'total_books': total_books, 'total_kategoris': total_kategoris})

@login_required
def Peminjam_buku_list(request):
    books = Buku.objects.all()
    return render(request, 'list_buku/Peminjam.html', {'books': books})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Set default role to 'Administrator' for newly registered user
            admin_group = Group.objects.get(name='Admin')
            user.groups.add(admin_group)
            return redirect('User:login')  # Ganti 'login' dengan nama URL untuk halaman login
    else:
        form = RegistrationForm()
    return render(request, 'auth/register.html', {'form': form})


# Buat view untuk logout
def user_logout(request):
    logout(request)  # Panggil fungsi logout dengan parameter request
    return redirect('User:login')  

def User_list(request):
    users = User.objects.all()
    return render(request, 'users/list.html', {'users': users})