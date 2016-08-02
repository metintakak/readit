from django import forms
from .models import Book

class ReviewForm(forms.Form):
    """
        form for reviewing a book
    """

    is_favoriote = forms.BooleanField(
        label = "Favorite?",
        help_text = "if it is in yor top 100 books of all time",
        required = False
    )

    review = forms.CharField(
        widget = forms.Textarea,
        min_length = 50,
        error_messages =  {
            'required' : 'Please enter your review',
            'min_length' : 'please enter at leats 50 characters. (you have written out %(show_value)s)'
        }
    )


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title','authors']
