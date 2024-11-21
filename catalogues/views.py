from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse

from django.views import generic
# Create your views here.
from .models import Book, BookInstance, Author, Languege, Genre

def index(reqeust):
    
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.count()
    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()

    context = {
        'num_books' :num_books,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available
    }
    return render(reqeust, 'catalogues/index.html', context = context)
    
    
class BookList(generic.ListView):
    model =  Book
    context_object_name =  'book_list'
    paginate_by = 2
    
    template_name = 'catalogue/book_list.html'


class BookDetail(generic.DetailView):
    model = Book
    context_object_name='book'
    template_name = 'catalogues/book_detail.html'

    def get_context_data(self, **kwargs):

        context = super(BookDetail, self).get_context_data(**kwargs)

        context['additional data'] = 'This is an additional data about the book model'

        return context
