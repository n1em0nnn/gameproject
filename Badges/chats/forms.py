from django import forms
from .models import Chat, Message
from teachers.models import ChildProfile

class AddParticipantForm(forms.Form):
    participant = forms.ModelChoiceField(queryset=ChildProfile.objects.all(), label="Add Participant")

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content', 'image']