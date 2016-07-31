from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def list_books(request):
    return render(request,"list.html")
    #you can access the login user information
    #return HttpResponse(request.user.username)
