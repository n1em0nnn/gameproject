from django.contrib.auth.backends import BaseBackend
from teachers.models import Teacher, ChildProfile

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Проверка для преподавателей
        try:
            teacher = Teacher.objects.get(user__username=username)
            if teacher.user.check_password(password):
                return teacher.user
        except Teacher.DoesNotExist:
            pass

        # Проверка для детей
        try:
            child = ChildProfile.objects.get(login=username)
            if child.password == password:
                # Создаем временного пользователя для ребенка
                from django.contrib.auth.models import User
                user, created = User.objects.get_or_create(username=f"child_{child.id}")
                user.set_password(child.password)
                user.save()
                return user
        except ChildProfile.DoesNotExist:
            pass

        return None

    def get_user(self, user_id):
        from django.contrib.auth.models import User
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None