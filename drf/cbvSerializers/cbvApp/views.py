
from django.shortcuts import render
from cbvApp.models import Student
from cbvApp.serializers import StudentSerializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework import mixins, generics
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class StudentPagination(LimitOffsetPagination):
    default_limit = 1
    max_limit = 5

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    pagination_class = StudentPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'id']

# Create your views here.
'''
class StudentList(generics.ListCreateAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Student.objects.all()
    serializer_class = StudentSerializers

'''
