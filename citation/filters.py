from django_filters import rest_framework as filters
from .models import Citation, Author, Category
from django.db import models


class CitationFilter(filters.FilterSet):
    search = filters.CharFilter(method="search_filter")

    def search_filter(self, queryset, name, value):
        return queryset.filter(
            models.Q(author__name__icontains=value.lower())
            | models.Q(citation__icontains=value.lower())
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
    author = filters.CharFilter(
        method='by_author'
    )

    def by_author(self, queryset, value, *args, **kwargs):
        author = Author.objects.get(id=args[0])
        citations = Citation.objects.filter(author=author)
        ids = []
        for c in citations:
            for cat in c.category.all():
                if cat.id not in ids:
                    ids.append(cat.id)
        return queryset.filter(id__in=ids)

    class Meta:
        model = Category
        fields = {
            "name": ["contains"],
        }
