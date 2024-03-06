from django.urls import path
from . import views

app_name = 'Ulasa'  # nama aplkasi

urlpatterns = [
    # Peminjam roles
    path('Ulasa/create/', views.create_Ulasa, name='create'),
    path('Ulasa/list/', views.Ulasa_list, name='read'),
    path('Ulasa/update/<str:koleksiid>/', views.update_Ulasa, name='update'),
    path('Ulasa/delete/<str:Koleksiid>/', views.delete_Ulasa, name='delete'),

]