from django.urls import path
from . import views

app_name = 'Ul'  # nama aplkasi

urlpatterns = [
    # Peminjam roles
    path('Ul/create/', views.create_Ul, name='create'),
    path('Ul/list/', views.Ul_list, name='read'),
    path('Ul/update/<str:koleksiid>/', views.update_Ul, name='update'),
    path('Ul/delete/<str:Koleksiid>/', views.delete_Ul, name='delete'),

]