from django.urls import path
from . import views

app_name = 'Ulasanbuku'  # nama aplkasi

urlpatterns = [
    # Peminjam roles
    path('ulasanbuku/create/<>', views.create_Ulasanbuku, name='create'),
    path('ulasanbuku/list/', views.Ulasanbuku_list, name='ulasan-read'),
    path('ulasanbuku/update/<str:koleksiid>/', views.update_Ulasanbuku, name='update'),
    path('ulasanbuku/delete/<str:Koleksiid>/', views.delete_Ulasanbuku, name='delete'),

]