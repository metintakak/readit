from django.contrib import admin
from .models import Book, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Book Details", {"fields":["title","authors"]}),
        ("Review", {"fields":["is_favoriote","review","date_reviewed"]}),
    ]

    readonly_fields = ["date_reviewed"]

    def book_authors(self, obj):
        return obj.list_authors();

    book_authors.short_description = "Authors"
    list_display = ("title","book_authors","date_reviewed","is_favoriote")
    list_editable = ["is_favoriote"]
    list_display_links = ("title","date_reviewed")
    list_filter = ["is_favoriote"]
    search_fields = ("title","authors__name",)

# Register your models here.
#instead of registering like this we can use register decorator
#admin.site.register(Book, BookAdmin)
admin.site.register(Author)
