from django.contrib import admin
from Books.models import BookstoreModel

# Register your models here.

class BookStoreModelAdmin(admin.ModelAdmin):
    list_display=('id','book_name','author','category','first_pub','last_pub')

admin.site.register(BookstoreModel,BookStoreModelAdmin)
