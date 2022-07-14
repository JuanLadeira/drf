from logging import raiseExceptions
from yaml import serialize
from products.serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    'DRF API VIEW'
    serializer =  ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        return Response(serializer.data)
    return Response({"invalid": "Not good data, try again"},status=400)
