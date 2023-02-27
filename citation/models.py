from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Categories"


class Citation(models.Model):
    citation = models.TextField(verbose_name="Citation")
    author = models.ForeignKey(
        Author,
        related_name="citations",
        on_delete=models.CASCADE,
        verbose_name="Author",
    )
    category = models.ManyToManyField(
        Category, related_name="citations", verbose_name="Categories"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.citation
