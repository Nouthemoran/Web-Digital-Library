from django.urls import path
from . import views

app_name = 'Peminjaman'  # nama aplkasi

urlpatterns = [
    # Peminjam roles
    path('peminjaman/create/<str:bukuid>/', views.create_Peminjaman, name='create'),
    path('peminjaman/list/', views.Peminjaman_list, name='admin-pinjam-read'),
    path('peminjaman/update/<str:peminjamanid>/', views.update_Peminjaman, name='update'),
    path('peminjaman/delete/<str:peminjamanid>/', views.delete_Peminjaman, name='delete'),

    # Admin roles
    path('peminjaman/admin/list/', views.admin_peminjalist, name='admin)
]