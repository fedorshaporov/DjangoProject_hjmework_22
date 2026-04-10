from django.urls import path
from .views import LoginView, LogoutView, RegisterView

app_name = 'users'  # Это пространство имен для пользователей

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),        # Страница для входа
    path('logout/', LogoutView.as_view(), name='logout'),     # Страница для выхода
    path('register/', RegisterView.as_view(), name='register'), # Страница для регистрации
]