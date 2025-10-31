# core/urls.py

from django.contrib import admin
from django.urls import path
from mgnrega import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('data/<str:district>/', views.district_data, name='district_data'),
    path('compare/', views.comparison, name='comparison'),
]
