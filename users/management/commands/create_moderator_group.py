from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from catalog.models import Product

class Command(BaseCommand):
    help = 'Создает группу модераторов продуктов и назначает права'

    def handle(self, *args, **kwargs):
        # Создание группы
        moderator_group, created = Group.objects.get_or_create(name='Модератор продуктов')

        # Назначение прав
        can_unpublish = Permission.objects.get(codename='can_unpublish_product')
        delete_product = Permission.objects.get(codename='delete_product')  # Убедитесь, что это правильное название
        moderator_group.permissions.add(can_unpublish)
        moderator_group.permissions.add(delete_product)

        self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" успешно создана и права назначены.'))