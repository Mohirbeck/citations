from rest_framework import generics
from .serializers import CitationSerializer, AuthorSerializer, CategorySerializer
from .models import Citation, Author, Category
from .filters import CitationFilter, AuthorFilter, CategoryFilter

# Create your views here.

class CitationListView(generics.ListCreateAPIView):
    queryset = Citation.objects.all()
    serializer_class = CitationSerializer
    filterset_class = CitationFilter

class CitationRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Citation.objects.all()
    serializer_class = CitationSerializer

class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_class = AuthorFilter

class AuthorRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class CategoryListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_class = CategoryFilter

class CategoryRetrieveView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
