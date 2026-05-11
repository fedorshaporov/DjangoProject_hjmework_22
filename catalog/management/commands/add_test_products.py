from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Adds test products to the database'

    def handle(self, *args, **kwargs):
        # Удаляем все существующие продукты
        Product.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all existing products.'))

        # Создаем тестовые категории, если они еще не существуют
        electronics, created = Category.objects.get_or_create(name="Электроника", description="Все, что связано с электроникой")
        clothing, created = Category.objects.get_or_create(name="Одежда", description="Модная одежда для всех")
        books, created = Category.objects.get_or_create(name="Книги", description="Разнообразные книги и литературные произведения")

        # Создаем тестовые продукты
        Product.objects.create(name="Смартфон", description="Современный смартфон с высокой производительностью.", category=electronics, price=699.99)
        Product.objects.create(name="Рубашка", description="Стильная рубашка для повседневной носки.", category=clothing, price=29.99)
        Product.objects.create(name="Роман", description="Интересный роман о приключениях и открытиях.", category=books, price=15.99)

        self.stdout.write(self.style.SUCCESS('Successfully added test products.'))
