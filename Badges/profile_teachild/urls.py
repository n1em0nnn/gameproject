from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile_view, name='profile_view'),
    path('edit-child/<int:child_id>/', views.edit_child_profile, name='edit_child_profile'),
]