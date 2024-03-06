from django.urls import path
from . import views

app_name = 'Koleksipribadi'  # nama aplkasi

urlpatterns = [
    # Peminjam roles
    path('koleksipribadi/create/', views.create_Koleksipribadi, name='create'),
    path('koleksipribadi/list/', views.Koleksipribadi_list, name='read'),
    path('koleksipribadi/update/<str:koleksiid>/', views.update_Koleksipribadi, name='update'),
    path('koleksipribadi/delete/<str:Koleksiid>/', views.delete_Koleksipribadi, name='delete'),

]