from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Chat, Message
from .forms import AddParticipantForm, MessageForm
from teachers.models import ChildProfile

# Проверка, является ли пользователь учителем или администратором
def is_teacher_or_admin(user):
    return hasattr(user, 'teacher') or user.is_staff

@login_required
def chat_list(request):
    if hasattr(request.user, 'childprofile'):
        chats = request.user.childprofile.chats.all()
    elif is_teacher_or_admin(request.user):
        chats = Chat.objects.all()
    else:
        chats = []
    return render(request, 'chats/chat_list.html', {'chats': chats})

@login_required
@user_passes_test(is_teacher_or_admin)
def add_participant(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    if request.method == 'POST':
        form = AddParticipantForm(request.POST)
        if form.is_valid():
            participant = form.cleaned_data['participant']
            chat.participants.add(participant)
            return redirect('chat_detail', chat_id=chat.id)
    else:
        form = AddParticipantForm()
    return render(request, 'chats/add_participant.html', {'form': form, 'chat': chat})

@login_required
@user_passes_test(is_teacher_or_admin)
def remove_participant(request, chat_id, participant_id):
    chat = get_object_or_404(Chat, id=chat_id)
    participant = get_object_or_404(ChildProfile, id=participant_id)
    chat.participants.remove(participant)
    return redirect('chat_detail', chat_id=chat.id)

@login_required
def chat_detail(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    if not (chat.participants.filter(id=request.user.childprofile.id).exists() or is_teacher_or_admin(request.user)):
        return render(request, 'chats/no_access.html')
    messages = chat.messages.all()
    if request.method == 'POST':
        form = MessageForm(request.POST, request.FILES)  # Добавляем request.FILES для обработки файлов
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.chat = chat
            message.save()
            return redirect('chat_detail', chat_id=chat.id)
    else:
        form = MessageForm()
    return render(request, 'chats/chat_detail.html', {'chat': chat, 'messages': messages, 'form': form})