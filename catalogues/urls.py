from .views import BookList, index, BookDetail

from django.urls import path

urlpatterns = [
    path('', index , name = 'home'),
    path('books', BookList.as_view(), name = 'books'),
    path('books/<int:pk>', BookDetail.as_view(), name='book-detail'),


]