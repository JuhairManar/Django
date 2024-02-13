from django.contrib import admin
from .models import Author, Book

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'display_authors', 'publication_date']
    list_filter = ['publication_date']
    search_fields = ['title', 'authors__name']

    def display_authors(self, obj):
        return ', '.join([author.name for author in obj.authors.all()])
    display_authors.short_description = 'Authors'
