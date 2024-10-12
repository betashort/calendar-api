from rest_framework import status, views
from rest_framework.response import Response

from .models import MentalHealthDirary
from .serializers import MentalHealthDiarySerializer

from django.shortcuts import render

# Create your views here.
class MentalHealthDiaryAPIView(views.APIView):
    
    def get(self, request, *arg, **kargs):
        mhd_event_list = MentalHealthDirary.objects.all()
        
        serializer = MentalHealthDiarySerializer(instance=mhd_event_list, many=True)
        
        return Response(serializer.data)
    
    def post(self, request, *arg, **kargs):
        
        serializer = MentalHealthDiarySerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status.HTTP_201_CREATED)