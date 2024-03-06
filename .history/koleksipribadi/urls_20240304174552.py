from django.urls import path
from . import views

app_name = 'Koleksipribadi'  # nama aplkasi

urlpatterns = [
    # Peminjam roles
    path('Koleksipribadi/create/', views.create_Koleksipribadi, name='create'),
    path('Koleksipribadi/list/', views.Koleksipribadi_list, name='read'),
    path('Koleksipribadi/update/<str:koleksiid>/', views.update_Koleksipribadi, name='update'),
    path('Koleksipribadi/delete/<str:Koleksiid>/', views.delete_Koleksipribadi, name='delete'),

]