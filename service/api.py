from .models import Service
from .serializers import ServiceSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def service_list_api(request):
    all_Service = Service.objects.all()
    data = ServiceSerializer(all_Service , many=True).data
    return Response({'data':data})


@api_view(['GET'])
def service_detail_api(request,id):
    Service_detail = Service.objects.get(id = id)
    data = ServiceSerializer(Service_detail).data
    return Response({'data': data})


class Service_list_Api(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class Service_detail_Api(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    lookup_fields = 'pk'

