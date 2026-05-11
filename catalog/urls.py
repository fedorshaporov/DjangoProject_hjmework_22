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
    CacheTestView,
    ProductByCategoryView,
)

app_name = CatalogConfig.name  # Используем название приложения для именования маршрутов

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Главная страница
    path('cache-test/', CacheTestView.as_view(), name='cache_test'),  # URL для тестирования кэша
    path('contacts/', ContactsView.as_view(), name='contacts'),  # Страница контактов
    path('product/list/', ProductListView.as_view(), name='product_list'),  # Список продуктов
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Детали продукта
    path('product/add/', ProductCreateView.as_view(), name='product_create'),  # Добавление продукта
    path('product/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),  # Редактирование продукта
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),  # Удаление продукта
    path('category/<int:category_id>/', ProductByCategoryView.as_view(), name='products_by_category'),  # Новый маршрут для получения продуктов по категории
]