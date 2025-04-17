from django.db import models
from django.contrib.auth.models import User
from teachers.models import Teacher, ChildProfile

class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,  # Разрешаем пустые значения
        blank=True  # Разрешаем пустые значения в формах
    )
    balance = models.PositiveIntegerField(default=0)  # Баланс пользователя

    def __str__(self):
        return self.user.username

class Product(models.Model):
    name = models.CharField(max_length=200)  # Название товара
    description = models.TextField()  # Описание товара
    price = models.PositiveIntegerField()  # Цена товара (в баллах)
    stock = models.PositiveIntegerField()  # Количество товара на складе

    def __str__(self):
        return self.name


class CartItem(models.Model):
    child_profile = models.ForeignKey(ChildProfile, on_delete=models.CASCADE, related_name='cart_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.child_profile.full_name} - {self.product.name}"


class Purchase(models.Model):
    child_profile = models.ForeignKey(ChildProfile, on_delete=models.CASCADE, related_name='purchases', null=True,  blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.PositiveIntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.child_profile.full_name} bought {self.product.name}"


class Notification(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='notifications')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.teacher.full_name}"