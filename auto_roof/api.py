from .models import Auto_Roof
from .serializers import Auto_RoofSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def auto_roof_list_api(request):
    all_Auto_Roof = Auto_Roof.objects.all()
    data = Auto_RoofSerializer(all_Auto_Roof , many=True).data
    return Response({'data':data})


@api_view(['GET'])
def auto_roof_detail_api(request,id):
    Auto_Roof_detail = Auto_Roof.objects.get(id = id)
    data = Auto_RoofSerializer(Auto_Roof_detail).data
    return Response({'data': data})


class Auto_Roof_list_Api(generics.ListCreateAPIView):
    queryset = Auto_Roof.objects.all()
    serializer_class = Auto_RoofSerializer


class Auto_Roof_detail_Api(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auto_Roof.objects.all()
    serializer_class = Auto_RoofSerializer
    lookup_fields = 'pk'

