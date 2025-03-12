from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('horses/', views.horse_index, name='horse-index'),
    path('horses/<int:horse_id>', views.horse_detail, name='horse-detail'),
    path('horses/create/', views.HorseCreate.as_view(), name='horse-create'),
    path('horses/<int:pk>/update', views.HorseUpdate.as_view(), name='horse-update'),
    path('horses/<int:pk>/delete', views.HorseDelete.as_view(), name='horse-delete'),
]
