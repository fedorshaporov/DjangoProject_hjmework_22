from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),  # Заканчивается на /
    path('', include('catalog.urls', namespace='catalog')),  # Заканчивается на /
    path('blog/', include('blog.urls', namespace='blog')),  # Заканчивается на /
]

# Добавляем обработку медиафайлов в режиме отладки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)