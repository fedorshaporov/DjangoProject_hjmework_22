from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, ProductDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Заканчивается на /
    path('contacts/', ContactsView.as_view(), name='contacts'),  # Заканчивается на /
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Заканчивается на /
]