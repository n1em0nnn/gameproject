from django import forms
from teachers.models import Teacher, ChildProfile

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['full_name', 'birth_year', 'direction']

class ChildProfileForm(forms.ModelForm):
    class Meta:
        model = ChildProfile
        fields = [
            'full_name',
            'birth_date',
            'phone_number',
            'training_group',
            'achievements',
            'parent_phone_number',
            'parent_name'
        ]