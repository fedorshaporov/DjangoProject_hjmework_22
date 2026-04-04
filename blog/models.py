from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)      # Заголовок
    content = models.TextField()                    # Содержимое
    preview_image = models.ImageField(upload_to='previews/')  # Превью (изображение)
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    is_published = models.BooleanField(default=False)  # Признак публикации
    views_count = models.PositiveIntegerField(default=0)  # Количество просмотров

    class Meta:
        ordering = ['-created_at']  # Сортировка по дате создания (последние записи первыми)
        verbose_name = 'Blog Post'  # Человекочитаемое имя в единственном числе
        verbose_name_plural = 'Blog Posts'  # Человекочитаемое имя во множественном числе
        db_table = 'blog_post'  # Имя таблицы в базе данных

    def __str__(self):
        return self.title