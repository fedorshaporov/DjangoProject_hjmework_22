from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Поле электронной почты для авторизации
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)  # Поле для аватара
    phone_number = models.CharField(max_length=15, blank=True, null=True)  # Поле для номера телефона
    country = models.CharField(max_length=100, blank=True, null=True)  # Поле для страны

    USERNAME_FIELD = 'email'  # Используйте email как поле для авторизации
    REQUIRED_FIELDS = ['username']  # Поля, которые требуются для создания пользователя (username остается, чтобы сохранить обратную совместимость)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
