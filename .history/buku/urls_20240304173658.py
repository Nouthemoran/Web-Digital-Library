from django.urls import path
from . import views

app_name = 'Koleksi'  # nama aplkasi

urlpatterns = [
    # Admin roles
    path('Koleksi/create/', views.create_Koleksi, name='create'),
    path('Koleksi/list/', views.Koleksi_list, name='read'),
    path('Koleksi/update/<str:Koleksiid>/', views.update_Koleksi, name='update'),
    path('Koleksi/delete/<str:Koleksiid>/', views.delete_Koleksi, name='delete'),

    # Peminjam roles
    path('peminjam/Koleksi/list/', views.Peminjam_Koleksi_list, name='peminjam-read'),
]