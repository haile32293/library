from .views import *

from django.urls import path

urlpatterns = [
    path('', index , name = 'home'),
    path('books', BookList.as_view(), name = 'books'),
    path('books/<int:pk>', BookDetail.as_view(), name='book-detail'),
    path('mybooks/', LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('loaned/', LoadnedBooks.as_view(), name='loaned'),


]