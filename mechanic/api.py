from .models import Mechanic
from .serializers import MechanicSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def mechanic_list_api(request):
    all_Mechanic = Mechanic.objects.all()
    data = MechanicSerializer(all_Mechanic , many=True).data
    return Response({'data':data})


@api_view(['GET'])
def mechanic_detail_api(request,id):
    Mechanic_detail = Mechanic.objects.get(id = id)
    data = MechanicSerializer(Mechanic_detail).data
    return Response({'data': data})


class Mechanic_list_Api(generics.ListCreateAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer


class Mechanic_detail_Api(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mechanic.objects.all()
    serializer_class = MechanicSerializer
    lookup_fields = 'pk'

