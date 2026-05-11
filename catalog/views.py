from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin  # Импортируем для ограничения доступа
from django.views.decorators.cache import cache_page  # Импортируйте кеш
from django.utils.decorators import method_decorator  # Импортируйте декоратор
from catalog.forms import ProductForm  # Импортируйте созданную вами форму
from django.core.cache import cache
from catalog.models import Product, Category  # Не забудьте импортировать Category
from django.http import Http404


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_products'] = Product.objects.order_by('-created_at')[:5]
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    # Добавляем кеширование для этого представления
    @method_decorator(cache_page(60 * 15))  # Кешируем страницу на 15 минут
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'  # Убедитесь, что этот шаблон существует
    context_object_name = 'products'

    def get_queryset(self):
        cache_key = 'product_list_cache'  # Уникальный ключ для кеша
        products = cache.get(cache_key)  # Попробуем получить данные из кеша
        if products is None:
            products = super().get_queryset()  # Если кеш пуст, получаем данные из базы данных
            cache.set(cache_key, products, timeout=60 * 10)  # Кешируем данные на 10 минут
        return products

class ProductCreateView(LoginRequiredMixin, View):
    template_name = 'product_form.html'

    def get(self, request, *args, **kwargs):
        form = ProductForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)  # Не сразу сохраняем
            product.owner = request.user  # Устанавливаем владельца продукта
            product.status = 'draft'  # Устанавливаем статус по умолчанию на черновик
            product.save()  # Сохраняем продукт
            messages.success(request, 'Продукт успешно добавлен.')
            return redirect('catalog:product_list')  # Убедитесь, что URL правильно ссылается
        return render(request, self.template_name, {'form': form})

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = 'product_form.html'

    def get(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт успешно обновлен.')
            return redirect('catalog:product_list')  # Убедитесь, что URL правильно ссылается
        return render(request, self.template_name, {'form': form})

    def test_func(self):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        return self.request.user == product.owner or self.request.user.has_perm('catalog.can_unpublish_product')

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    template_name = 'product_confirm_delete.html'

    def get(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        return render(request, self.template_name, {'product': product})

    def post(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        messages.success(request, 'Продукт успешно удален.')
        return redirect('catalog:product_list')  # Убедитесь, что URL правильно ссылается

    def test_func(self):
        product = get_object_or_404(Product, pk=self.kwargs['pk'])
        return self.request.user == product.owner or self.request.user.has_perm('catalog.delete_product')

class ContactsView(View):
    template_name = 'contacts.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        if not name or not phone or not message:
            return render(request, self.template_name, {'error': 'Пожалуйста, заполните все поля.'})

        messages.success(request, 'Ваше сообщение успешно отправлено!')
        return render(request, 'contact_success.html', {'name': name})

class CacheTestView(View):
    def get(self, request):
            # Пробуем получить данные из кэша
        cached_data = cache.get('my_key')
        if not cached_data:
            # Если данных нет, можем их создать
            cached_data = 'Некоторые данные, которые нужно кэшировать'
            cache.set('my_key', cached_data, timeout=60 * 15)  # Кэшируем данные на 15 минут

        return render(request, 'cache_test.html', {'data': cached_data})  # Используйте ваш шаблон

def get_products_by_category(category_id):
    try:
        # Получаем категорию по ID
        category = Category.objects.get(id=category_id)
        return Product.objects.filter(category=category)  # Возвращаем продукты для этой категории
    except Category.DoesNotExist:
        return Product.objects.none()  # Если категория не найдена, возвращаем пустой queryset


class ProductByCategoryView(ListView):
    model = Product
    template_name = 'products_by_category.html'  # Шаблон для отображения продуктов категории
    context_object_name = 'products'

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')  # Получаем ID категории из URL
        cache_key = f'products_by_category_{category_id}'  # Уникальный ключ для кеша
        products = cache.get(cache_key)  # Попробуем получить данные из кеша
        if products is None:
            products = get_products_by_category(category_id)  # Получаем продукты по категории
            if not products:
                raise Http404("Категория не найдена или в ней нет продуктов.")  # Возвращаем 404, если ничего не найдено
            cache.set(cache_key, products, timeout=60 * 10)  # Кешируем данные на 10 минут
        return products


