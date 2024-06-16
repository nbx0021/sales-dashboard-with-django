from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('show_data/', views.show_data, name='show_data'),
    path('dashboard/', views.dashboard, name='dashboard'),  
    path('get_data/', views.get_data, name='get_data'),
]
