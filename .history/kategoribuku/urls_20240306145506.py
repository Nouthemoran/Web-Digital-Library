from django.urls import path
from . import views

app_name = 'Kategoribuku'  # nama aplkasi

urlpatterns = [
    # Admin roles
    path('kategoribuku/create/', views.create_Kategoribuku, name='create'),
    path('kategoribuku/list/', views.Kategoribuku_list, name='read'),
    path('kategoribuku/update/<str:kategoriid>/', views.update_Kategoribuku, name='update'),
    path('kategoribuku/delete/<str:kategoriid>/', views.delete_Kategoribuku, name='delete'),

    # Peminjam roles
    path('peminjam/kategoribuku/list/', views.Peminjam_Kategoribuku_list, name='kategori-read'),
     path('list/<str:kategoriid>/', views.lihat_buku_per_kategori, name='list_kategoribuku'),
]