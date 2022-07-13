import imp
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


# Create your views here.

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)


class ProductDetailAPIView(generics.RetrieveAPIView):  # MOSTRA OS DETALHES DOS PRODUTOS
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductListAPIView(generics.ListAPIView):
    # NÃO SERÁ USADO.
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
