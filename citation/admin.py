from django.contrib import admin
from .models import Author, Category, Citation

# Register your models here.

admin.site.register(Author)
admin.site.register(Category)

@admin.register(Citation)
class CitationAdmin(admin.ModelAdmin):
    list_display = ["citation", "author", "categories"]
    list_filter = ["author", "category"]
    search_fields = ["citation", "author__name", "category__name"]
    
    def categories(self, obj):
        return ", ".join([c.name for c in obj.category.all()])
    
    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "category":
            kwargs["queryset"] = Category.objects.all()
        return super().formfield_for_manytomany(db_field, request, **kwargs)