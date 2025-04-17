from django.db import models
from django.contrib.auth.models import User
from teachers.models import ChildProfile

class Chat(models.Model):
    name = models.CharField(max_length=200)  # Название чата
    description = models.TextField(blank=True, null=True)  # Описание чата
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    participants = models.ManyToManyField(ChildProfile, related_name='chats')  # Участники чата (ученики)
    is_private = models.BooleanField(default=False)  # Флаг приватности (только для учителей)

    def __str__(self):
        return self.name


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')  # Чат
    sender = models.ForeignKey(User, on_delete=models.CASCADE)  # Отправитель (учитель или ученик)
    content = models.TextField()  # Текст сообщения
    image = models.ImageField(upload_to='chat_images/', blank=True, null=True)  # Прикрепленное изображение
    timestamp = models.DateTimeField(auto_now_add=True)  # Время отправки

    def __str__(self):
        return f"Message by {self.sender.username} in {self.chat.name}"