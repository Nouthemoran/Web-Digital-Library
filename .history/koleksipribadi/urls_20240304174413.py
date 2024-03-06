from django.urls import path
from . import views

app_name = ''  # nama aplkasi

urlpatterns = [
    # Admin roles
    path('/create/', views.create_, name='create'),
    path('/list/', views._list, name='read'),
    path('/update/<str:id>/', views.update_, name='update'),
    path('/delete/<str:id>/', views.delete_, name='delete'),

    # Peminjam roles
    path('peminjam//list/', views.Peminjam__list, name='peminjam-read'),
]