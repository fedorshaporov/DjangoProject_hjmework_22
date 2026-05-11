from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import CustomUser
from .forms import CustomUserCreationForm

class LoginView(BaseLoginView):
    template_name = 'login.html'  # Укажите ваш шаблон для входа
    redirect_authenticated_user = True  # Перенаправление для аутентифицированных пользователей

    def form_valid(self, form):
        return super().form_valid(form)

class LogoutView(BaseLogoutView):
    next_page = reverse_lazy('catalog:home')  # Перенаправление на главную страницу после выхода

class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'register.html'  # Укажите ваш шаблон для регистрации
    success_url = reverse_lazy('catalog:home')  # Перенаправление после успешной регистрации

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  # Вход пользователя после регистрации
        # Отправка приветственного письма
        send_mail(
            'Добро пожаловать на SkyStore!',
            'Спасибо за регистрацию на нашем сайте! Мы рады вас видеть.',
            'noreply@yourdomain.com',  # Замените на свой адрес отправителя
            [user.email],
            fail_silently=False,
        )
        return super().form_valid(form)