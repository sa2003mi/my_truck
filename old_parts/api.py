from .models import Old_Parts
from .serializers import Old_PartsSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics


@api_view(['GET'])
def old_parts_list_api(request):
    all_Old_Parts = Old_Parts.objects.all()
    data = Old_PartsSerializer(all_Old_Parts , many=True).data
    return Response({'data':data})


@api_view(['GET'])
def old_parts_detail_api(request,id):
    Old_Parts_detail = Old_Parts.objects.get(id = id)
    data = Old_PartsSerializer(Old_Parts_detail).data
    return Response({'data': data})


class Old_Parts_list_Api(generics.ListCreateAPIView):
    queryset = Old_Parts.objects.all()
    serializer_class = Old_PartsSerializer


class Old_Parts_detail_Api(generics.RetrieveUpdateDestroyAPIView):
    queryset = Old_Parts.objects.all()
    serializer_class = Old_PartsSerializer
    lookup_fields = 'pk'

