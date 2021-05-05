""""
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from ..models import About, SubDescription
from .serializers import AboutSerializer

class AboutPageView(APIView):
    def get(self,request,format=None):
        about_us=About.objects.all()
        serializer =AboutSerializer(about_us,many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        serializer=AboutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
""""
