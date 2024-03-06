from django.urls import path
from . import views

app_name = 'Koleksipribadi'  # nama aplkasi

urlpatterns = [
    # Admin roles
    path('Koleksipribadi/create/', views.create_Koleksipribadi, name='create'),
    path('Koleksipribadi/list/', views.Koleksipribadi_list, name='read'),
    path('Koleksipribadi/update/<str:kolekisid>/', views.update_Koleksipribadi, name='update'),
    path('Koleksipribadi/delete/<str:Koleksipribadiid>/', views.delete_Koleksipribadi, name='delete'),

    # Peminjam roles
    path('peminjam/Koleksipribadi/list/', views.Peminjam_Koleksipribadi_list, name='peminjam-read'),
]