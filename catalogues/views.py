from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Book, BookInstance, Author, Languege, Genre

def index(request):
        num_books = Book.objects.all().count()
        num_instances = BookInstance.objects.all().count()
        num_instances_available = BookInstance.objects.filter(status__exact = 'a'
                                                              ).count()
        
        conteext = {
                'num_books' : num_books,
                'num_instance':num_instances,
                'num_instances_available':num_instances_available
        }
        
        return render(request, 'catalogues/index.html', context=conteext)