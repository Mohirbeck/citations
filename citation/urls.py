from django.urls import path

from . import views

app_name = "citation"

urlpatterns = [
    path("citations/", views.CitationListView.as_view(), name="list"),
    path("citations/<int:pk>/", views.CitationRetrieveView.as_view(), name="detail"),
    path("authors/", views.AuthorListView.as_view(), name="author_list"),
    path("authors/<int:pk>/", views.AuthorRetrieveView.as_view(), name="author_detail"),
    path("categories/", views.CategoryListView.as_view(), name="category_list"),
    path("categories/<int:pk>/", views.CategoryRetrieveView.as_view(), name="category_detail"),
]
