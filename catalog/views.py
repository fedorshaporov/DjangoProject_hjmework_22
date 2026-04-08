from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, DetailView, ListView
from django.contrib import messages
from catalog.models import Product
from catalog.forms import ProductForm  # Импортируйте созданную вами форму
from django.core.exceptions import ValidationError

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

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'  # Убедитесь, что этот шаблон существует
    context_object_name = 'products'


class ProductCreateView(View):
    template_name = 'product_form.html'

    def get(self, request, *args, **kwargs):
        form = ProductForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalog:product_list')  # Убедитесь, что 'product_list' правильно ссылается на маршрут
        return render(request, self.template_name, {'form': form})


class ProductUpdateView(View):
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
            return redirect('catalog:product_list')  # Убедитесь, что это правильно
        return render(request, self.template_name, {'form': form})

class ProductDeleteView(View):
    template_name = 'product_confirm_delete.html'

    def get(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        return render(request, self.template_name, {'product': product})

    def post(self, request, pk, *args, **kwargs):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        messages.success(request, 'Продукт успешно удален.')
        return redirect('product_list')

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

        return render(request, 'contact_success.html', {'name': name})