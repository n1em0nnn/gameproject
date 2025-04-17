from django import forms
from .models import Achievement

class AchievementForm(forms.ModelForm):
    class Meta:
        model = Achievement
        fields = ['name', 'description', 'reward', 'how_to_unlock', 'icon']