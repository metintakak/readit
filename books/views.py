from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from .models import Book, Author
from django.views.generic import DetailView, View
from django.db.models import Count
from .forms import ReviewForm, BookForm
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView

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

# Paste into Views.py - don't forget to import get_object_or_404!
class ReviewList(View):
    """
    List all of the books that we want to review.
    """

    def get(self,request):
        books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')

        context = {
        	'books': books,
            'form' : BookForm,
        }

        return render(request, "list-to-review.html", context)

    def post(self,request):
        form = BookForm(request.POST)
        books = Book.objects.filter(date_reviewed__isnull=True).prefetch_related('authors')
        if form.is_valid():
            form.save()
            return redirect('review-books')

        context = {
        	'books': books,
            'form' : form,
        }
        return render(request, "list-to-review.html", context)



def review_book(request, pk):
    """
    Review an individual book
    """
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            book.is_favoriote = form.cleaned_data['is_favoriote']
            book.review = form.cleaned_data['review']
            book.reviewed_by = request.user
            book.save()
            return redirect('review_books')
    else:
        form = ReviewForm

    context = {
    	'book': book,
        'form' : form,
    }

    return render(request, "review-book.html", context)


class CreateAuthor(CreateView):
    model = Author
    fields = ['name',]
    template_name = "create-author.html"
    def get_success_url(self):
        return reverse('review-books')
