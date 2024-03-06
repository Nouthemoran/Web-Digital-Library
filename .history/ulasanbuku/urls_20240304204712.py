from django.urls import path
from . import views

app_name = ''  # nama aplkasi

urlpatterns = [
    # Peminjam roles
    path('/create/', views.create_, name='create'),
    path('/list/', views._list, name='read'),
    path('/update/<str:koleksiid>/', views.update_, name='update'),
    path('/delete/<str:Koleksiid>/', views.delete_, name='delete'),

]