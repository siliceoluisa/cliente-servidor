from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from django.http import Http404
from django.shortcuts import get_object_or_404

#Importaciones de modelos
from Example1.models import Example1

#Importaciones de Serializers
from Example1.serializer import Example1Serializers


class ExampleList(APIView):
    def get(self, request, format=None):
        print("GET")
        queryset= Example1.objects.all()
        serializer= Example1Serializers(queryset, many= True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer= Example1Serializers(data= request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
# Create your views here.
