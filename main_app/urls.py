from django.urls import path
from . import views 
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('horses/', views.horse_index, name='horse_index'),
    path('horses/<int:horse_id>', views.horse_detail, name='horse_detail'),
]
