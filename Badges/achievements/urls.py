from django.urls import path
from . import views

urlpatterns = [
    path('', views.achievement_list, name='achievement_list'),
    path('<int:achievement_id>/', views.achievement_detail, name='achievement_detail'),
]