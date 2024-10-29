from rest_framework.generics import ListAPIView, RetrieveAPIView
from .product_serializers import ProductListSerializer, ProductDetailsSerializer
from main.models import Product, Review


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailsView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailsSerializer
    lookup_field = 'id'


