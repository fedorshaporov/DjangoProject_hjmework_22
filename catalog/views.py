from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView, DetailView
from catalog.models import Product

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