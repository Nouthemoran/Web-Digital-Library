from django.urls import path
from . import views

app_name = 'Buku'  # nama aplkasi

urlpatterns = [
    # Admin roles
    path('buku/create/', views.create_Buku, name='create'),
    path('buku/list/', views.Buku_list, name='buku-read'),
    path('buku/update/<str:bukuid>/', views.update_Buku, name='update'),
    path('buku/delete/<str:bukuid>/', views.delete_Buku, name='delete'),

    # Peminjam roles
    path('peminjam/buku/list/', views.Peminjam_buku_list, name='peminjam-read'),
]