from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Author
from django.views.generic import DetailView, View
from django.db.models import Count

# Create your views here.
def list_books(request):
    """
    list the books that has reviews
    """

    books = Book.objects.exclude(date_reviewed__isnull=True).prefetch_related('authors')
    context = {
        "books" : books,
    }

    return render(request,"list.html",context)
    #you can access the login user information
    #return HttpResponse(request.user.username)


class AuthorList(View):
    def get(self,request):
        #to select all authors
        #authors = Author.objects.all()

        #to select authors who only have books
        authors = Author.objects.annotate(
            published_books = Count('books')
        ).filter(
            published_books__gt=0
        )
        context = {
            "authors" : authors
        }

        return render(request,"authors.html",context)

class BookDetail(DetailView):
    model = Book
    template_name = "book.html"


class AuthorDetail(DetailView):
    model = Author
    template_name = "author.html"    
