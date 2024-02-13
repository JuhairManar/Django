from django.urls import path
from .views import AuthorListCreateAPIView, AuthorRetrieveUpdateDestroyAPIView, \
    BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('', AuthorListCreateAPIView.as_view(), name='home'),  # Define a URL pattern for the root URL
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorRetrieveUpdateDestroyAPIView.as_view(), name='author-detail'),
    path('books/', BookListCreateAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
    path('docs/', include_docs_urls(title='Bookstore API')),
    path('schema/', get_schema_view(
        title="Bookstore API",
        description="API for managing books and authors",
        version="1.0.0"
    ), name='openapi-schema'),
]

