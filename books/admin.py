from django.contrib import admin
from .models import Book,Articles
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Articles)
class BookAdmin(admin.ModelAdmin):
    pass
