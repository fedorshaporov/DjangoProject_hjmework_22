from django.contrib import admin
from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  # Поля для отображения в списке категорий

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')  # Поля для отображения в списке продуктов
    list_filter = ('category',)  # Фильтрация по категории
    search_fields = ('name', 'description')  # Поиск по полям name и description

# Регистрация моделей в админке Django
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)