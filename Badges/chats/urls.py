from django.urls import path
from . import views

urlpatterns = [
    path('', views.chat_list, name='chat_list'),
    path('<int:chat_id>/', views.chat_detail, name='chat_detail'),
    path('<int:chat_id>/add-participant/', views.add_participant, name='add_participant'),
    path('<int:chat_id>/remove-participant/<int:participant_id>/', views.remove_participant, name='remove_participant'),
]