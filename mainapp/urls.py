
from django.urls import path
from .views import tets_view, ProductDetailView

urlpatterns = [
    path('', tets_view, name='base'),
    path('products/<str:ct_model>/<str:slug>', ProductDetailView.as_view(), name='product_detail')
]

