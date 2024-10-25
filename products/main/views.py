from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from main.serializers import ProductListSerializer, ProductDetailsSerializer
from main.models import Product, Review
from django.http import Http404


@api_view(['GET'])
def products_list_view(request):
    """реализуйте получение всех товаров из БД
    реализуйте сериализацию полученных данных
    отдайте отсериализованные данные в Response"""
    products = Product.objects.all()
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)


class ProductDetailsView(APIView):
    def get(self, request, product_id):
        """реализуйте получение товара по id, если его нет, то выдайте 404
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        try:
            product = Product.objects.get(pk=product_id)
        except Product.DoesNotExist:
            raise Http404('Продукт не найден')

        serializer = ProductDetailsSerializer(product)
        return Response(serializer.data)

