from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action

from .models import *
from .serializers import *
# Create your views here.
class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

    def get_queryset(self):
        return Status.objects.all()
    
    def list(self, request, *args, **kwargs):
        try:
            #search_query = request.query_params.get('search', '')
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({"success":True, "message":"List retrieved successfully", "data":serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"success":False, "message":"Something went wrong. Please try again later.", "data":None, "errors":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def create(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({"success":True, "message":"Created successfully", "data":serializer.data}, status=status.HTTP_201_CREATED, headers=headers)
        except Exception as e:
            return Response({"success":False, "message":"Something went wrong. Please try again later.", "data":None, "errors":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
        
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({"success":True, "message":"Retrieved successfully", "data":serializer.data}, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True, "message": "Updated successfully", "data": serializer.data}, status=status.HTTP_200_OK)
        return Response({"success": False, "message": "Validation error", "data":None, "errors":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None, format=None):
        instance = self.get_object(pk)
        instance.delete()
        return Response({"success": True, "message": "deleted successfully"},status=status.HTTP_204_NO_CONTENT)