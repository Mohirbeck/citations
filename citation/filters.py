from django_filters import rest_framework as filters
from .models import Citation, Author, Category
from django.db import models


class CitationFilter(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            models.Q(author__name__icontains=value)
            | models.Q(citation__icontains=value)
        )
    class Meta:
        model = Citation
        fields = {
            "category": ["exact"],
            "author": ["exact"],
        }

class AuthorFilter(filters.FilterSet):
    class Meta:
        model = Author
        fields = {
            "name": ["contains"],
        }

class CategoryFilter(filters.FilterSet):
    author = filters.ModelChoiceFilter(
        field_name="citations__author",
        queryset=Author.objects.all(),
        to_field_name="id",
    )

    class Meta:
        model = Category
        fields = {
            "name": ["contains"],
        }
