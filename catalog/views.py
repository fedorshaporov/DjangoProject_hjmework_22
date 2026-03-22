from django.shortcuts import render, get_object_or_404

from catalog.models import Product, Category

def home(request):
    # Получаем последние 5 продуктов
    latest_products = Product.objects.order_by('-created_at')[:5]
    return render(request, 'home.html', {'latest_products': latest_products})

def product_detail(request, product_id):
    # Получаем продукт по ID
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'catalog/product_detail.html', {'product': product})

def contacts(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        # Проверка на None или пустые значения (более безопасно)
        if not name or not phone or not message:
            return render(request, 'contacts.html', {'error': 'Пожалуйста, заполните все поля.'})

        return render(request, 'contact_success.html', {'name': name})

    return render(request, 'contacts.html')