from django.shortcuts import render
from django.http import HttpResponse
from .models import Book

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
