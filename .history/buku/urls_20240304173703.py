from django.urls import path
from . import views

app_name = 'Koleksiprida'  # nama aplkasi

urlpatterns = [
    # Admin roles
    path('Koleksiprida/create/', views.create_Koleksiprida, name='create'),
    path('Koleksiprida/list/', views.Koleksiprida_list, name='read'),
    path('Koleksiprida/update/<str:Koleksipridaid>/', views.update_Koleksiprida, name='update'),
    path('Koleksiprida/delete/<str:Koleksipridaid>/', views.delete_Koleksiprida, name='delete'),

    # Peminjam roles
    path('peminjam/Koleksiprida/list/', views.Peminjam_Koleksiprida_list, name='peminjam-read'),
]