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
    path('horses/<int:horse_id>/add_feeding/', views.add_feeding, name='add-feeding'),
    path('trainings/create/', views.TrainingCreate.as_view(), name='training-create'),
    path('training/<int:pk>/', views.TrainingDetail.as_view(), name='training-detail'),
    path('trainings/', views.TrainingList.as_view(), name='training-index'),
    path('training/<int:pk>/update/', views.TrainingUpdate.as_view(), name='training-update'),
    path('training/<int:pk>/delete/', views.TrainingDelete.as_view(), name='training-delete'),
    path('horses/<int:horse_id>/associate_training/<int:training_id>/', views.associate_training, name='associate-training'),
    path('horses/<int:horse_id>/remove-training/<int:training_id>/', views.remove_training, name='remove-training'),
]
