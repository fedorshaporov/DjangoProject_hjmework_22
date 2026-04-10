from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import (
    HomeView,
    ContactsView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductListView,
)

app_name = CatalogConfig.name  # Используем название приложения для именования маршрутов

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Главная страница
    path('contacts/', ContactsView.as_view(), name='contacts'),  # Страница контактов
    path('product/list/', ProductListView.as_view(), name='product_list'),  # Список продуктов
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Детали продукта
    path('product/add/', ProductCreateView.as_view(), name='product_create'),  # Добавление продукта
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),  # Редактирование продукта
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),  # Удаление продукта
]