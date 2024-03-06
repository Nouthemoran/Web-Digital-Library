from django.urls import path
from . import views

app_name = 'Ulasan'  # nama aplkasi

urlpatterns = [
    # Peminjam roles
    path('Ulasan/create/', views.create_Ulasan, name='create'),
    path('Ulasan/list/', views.Ulasan_list, name='read'),
    path('Ulasan/update/<str:koleksiid>/', views.update_Ulasan, name='update'),
    path('Ulasan/delete/<str:Koleksiid>/', views.delete_Ulasan, name='delete'),

]