from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Teacher, ChildProfile

class TeacherRegistrationForm(UserCreationForm):
    full_name = forms.CharField(max_length=200)
    birth_year = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'full_name', 'birth_year', 'password1', 'password2']
class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['full_name', 'birth_year', 'direction']

class ChildProfileForm(forms.ModelForm):
    class Meta:
        model = ChildProfile
        fields = ['full_name', 'birth_date', 'phone_number', 'training_group']