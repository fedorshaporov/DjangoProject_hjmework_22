from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # URL для административной панели
    path('users/', include('users.urls', namespace='users')),  # Namespace для URL пользователей
    path('', include('catalog.urls', namespace='catalog')),  # Основные маршруты каталога
    path('blog/', include('blog.urls', namespace='blog')),  # URL для блога (если есть)
]

# Добавляем обработку медиафайлов в режиме отладки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)