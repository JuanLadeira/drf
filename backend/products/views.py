from dataclasses import dataclass
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import  authentication, generics, permissions
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

#Lista e cria os dados na api.
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content')
        if content is None:
            content = title
        serializer.save(content=content)

#Mostra os detalhes dos dados que forem solicitados.
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

#Atualiza os dados que forem consultados
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field= 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

#Deleta os dados que foram solicitados.
class ProductDestroyAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer   
    lookup_field= 'pk' 

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

      
# METODO QUE SERIA UTILIZADO CASO NÃO FOSSE UTILIZAR generics.views.
# Eu precisaria codar muito mais do que nas classes acima.
# This method below would be used if I wouldn't use the generis.views, as you can see below,
# I would have to write more code then, the generis.views are easier to use.

@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    method = request.method
    if method == 'GET': #caso seja o metodo "GET" / "PEGAR OU CONSULTAR".
        if pk is not None: # caso a ID solicitada não seja nula, a API retornará os dados referentes a ID em questão.
            # detailview
            obj = get_object_or_404(Product, pk=pk) #Caso o objeto não exista, retornará erro 404 "objeto não encontrado".
            data = ProductSerializer(obj).data #Trata os dados antes de envia-los
            return Response(data) #retorna os dados caso eles se encontrem no banco de dados
        #listview 
        # Caso a ID seja NULA, ou seja, não tenha sido fornecido uma, a api retornara a lista de dados do BD.
        queryset = Product.objects.all() #Atribuição da fila de dados que será mostrada ao solicitante
        data = ProductSerializer(queryset, many=True).data #tratamento dos dados
        return Response(data) #retorna os dados da fila.
    
    # Caso o metodo seja "POST" / "POSTAR OU ENVIAR"
    if method == 'POST': 
        serializer = ProductSerializer(data=request.data) #Valida os dados que estão sendo enviados, verificando os pré-requesitos
        #caso os dados sejam validos, serão salvos no banco de dados.
        if serializer.is_valid(raise_exception=True): #raise_exception=True Mostra ao usuario qual dado não está valido. 
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content')
            if content is None: #caso o conteudo seja nulo, a api atribuirá o conteudo igual ao titulo.
                content = title
            serializer.save(content=content) #salva os dados.
            return Response(serializer.data) #retorna os dados que foram salvos
        #caso os dados não forem validos a API retornará que os dados não são bons sem demonstrar onde está o problema.    
        return Response({"invalid": "Not good data, try again"}, status=400)
