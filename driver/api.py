from .models import Driver
from .serializers import DriverSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def driver_list_api(request):
    all_Driver = Driver.objects.all()
    data = DriverSerializer(all_Driver , many=True).data
    return Response({'data':data})


@api_view(['GET'])
def driver_detail_api(request,id):
    Driver_detail = Driver.objects.get(id = id)
    data = DriverSerializer(Driver_detail).data
    return Response({'data': data})


class Driver_list_Api(generics.ListCreateAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class Driver_detail_Api(generics.RetrieveUpdateDestroyAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    lookup_fields = 'pk'

