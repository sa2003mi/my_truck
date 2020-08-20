from .models import Spare_Parts
from .serializers import Spare_PartsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def spare_parts_list_api(request):
    all_Old_Parts =Spare_Parts.objects.all()
    data =Spare_PartsSerializer(all_Old_Parts , many=True).data
    return Response({'data':data})


@api_view(['GET'])
def spare_parts_detail_api(request,id):
    Spare_Parts_detail =Spare_Parts.objects.get(id = id)
    data =Spare_PartsSerializer(Spare_Parts_detail).data
    return Response({'data': data})


class Spare_Parts_list_Api(generics.ListCreateAPIView):
    queryset =Spare_Parts.objects.all()
    serializer_class =Spare_PartsSerializer


class Spare_Parts_detail_Api(generics.RetrieveUpdateDestroyAPIView):
    queryset =Spare_Parts.objects.all()
    serializer_class =Spare_PartsSerializer
    lookup_fields = 'pk'

