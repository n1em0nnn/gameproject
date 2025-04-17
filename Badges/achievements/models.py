from django.db import models
from teachers.models import ChildProfile

class Achievement(models.Model):
    name = models.CharField(max_length=200)  # Название достижения
    description = models.TextField()  # Описание достижения
    reward = models.CharField(max_length=200)  # Награда за достижение
    how_to_unlock = models.TextField()  # Как получить достижение
    icon = models.ImageField(upload_to='achievements_icons/', blank=True, null=True)  # Иконка достижения

    def __str__(self):
        return self.name


class ChildAchievement(models.Model):
    child = models.ForeignKey(
        ChildProfile,
        on_delete=models.CASCADE,
        related_name='child_achievements'  # Уникальное имя для обратной связи
    )
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    unlocked = models.BooleanField(default=False)  # Статус разблокировки
    unlock_date = models.DateField(blank=True, null=True)  # Дата получения

    def __str__(self):
        return f"{self.child.full_name} - {self.achievement.name}"