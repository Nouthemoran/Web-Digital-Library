from django.urls import path
from . import views

app_name = 'Ulasanbuku'  # nama aplkasi

urlpatterns = [
    # Peminjam roles
    path('Ulasanbuku/create/', views.create_Ulasanbuku, name='create'),
    path('Ulasanbuku/list/', views.Ulasanbuku_list, name='read'),
    path('Ulasanbuku/update/<str:koleksiid>/', views.update_Ulasanbuku, name='update'),
    path('Ulasanbuku/delete/<str:Koleksiid>/', views.delete_Ulasanbuku, name='delete'),

]