from django.db import models
from django.contrib.auth.models import User

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    birth_year = models.PositiveIntegerField()
    direction = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.full_name

class ChildProfile(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='children')
    full_name = models.CharField(max_length=200)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=15)
    training_group = models.CharField(max_length=100)
    achievements = models.TextField(blank=True, null=True)  # Заработанные достижения
    parent_phone_number = models.CharField(max_length=15, blank=True, null=True)  # Номер телефона родителя
    parent_name = models.CharField(max_length=200, blank=True, null=True)  # Имя и отчество родителя
    login = models.CharField(max_length=50, unique=True)  # Логин для ребенка
    password = models.CharField(max_length=128)  # Пароль для ребенка
    points = models.PositiveIntegerField(default=0)  # Валюта ученика

    def __str__(self):
        return self.full_name