from django.shortcuts import render
from rest_framework import generics
from .models import Book, Author
from nsApp.serializer import BookSerializer, AuthorSerializer, AuthorBookSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

# Create your views here.
class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorBookListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorBookSerializer

