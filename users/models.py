from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    """Модель пользователя, расширяющая стандартную модель Django."""

    email = models.EmailField(unique=True, verbose_name="Электронная почта")  # Поле электронной почты для авторизации
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name="Аватар")  # Поле для аватара
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Номер телефона")  # Поле для номера телефона
    country = models.CharField(max_length=100, blank=True, null=True, verbose_name="Страна")  # Поле для страны

    # Настройки для аутентификации
    USERNAME_FIELD = 'email'  # Используйте email как поле для авторизации
    REQUIRED_FIELDS = ['username']  # Поля, необходимые при создании пользователя

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        """Строковое представление модели пользователя."""
        return self.email  # Составляем строковое представление по email