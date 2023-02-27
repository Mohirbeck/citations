from rest_framework import serializers
from .models import Citation, Author, Category


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CitationSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["author"] = AuthorSerializer(instance.author).data
        data["category"] = CategorySerializer(instance.category, many=True).data
        return data

    class Meta:
        model = Citation
        fields = "__all__"
