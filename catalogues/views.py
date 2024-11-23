from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.views import generic
# Create your views here.
from .models import Book, BookInstance, Author, Languege, Genre

def index(reqeust):

    num_views = reqeust.session.get('num_visit',0)
    num_views +=1 

    reqeust.session['num_visit'] = num_views

    
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.count()
    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()

    context = {
        'num_books' :num_books,
        'num_instances':num_instances,
        'num_instances_available':num_instances_available,
        'num_views': num_views
    }
    return render(reqeust, 'catalogues/index.html', context = context)
    
    
class BookList(LoginRequiredMixin, generic.ListView):
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
    

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
    template_name = 'catalogues/books_by_borrower.html'
    model = BookInstance

    def get_queryset(self):

        return BookInstance.objects.filter(borrower = self.request.user).filter(status__exact='o').order_by('due_back')

class LoadnedBooks(LoginRequiredMixin,PermissionRequiredMixin,generic.ListView):
    permission_required = 'catalogues.can_mark_returned'
    template_name = 'catalogues/loanedbooks.html'
    model = BookInstance
    context_object_name = 'books'

    def get_queryset(self):

        return BookInstance.objects.filter(status__exact = 'o')
