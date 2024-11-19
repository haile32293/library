from django.contrib import admin

# Register your models here.
from .models import Book, BookInstance, Author, Genre, Languege


class BookInstanceInlines(admin.TabularInline):
    model = BookInstance

class BookInlines(admin.TabularInline):
    model = Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','date_of_birth','date_of_death']
    #fields = ['first_name','last_name',('date_of_birth', 'date_of_death')]
    inlines =[BookInlines,]




@admin.register(BookInstance)
class BookinstanceAdmin(admin.ModelAdmin):
    list_display = ['book','status','due_back']
    list_filter = ['status', 'due_back']

    
    fieldsets= (
        (None,
         {
             'fields': ('book', 'imprint','id') 
         }),
         (
         'Availabilty',
         {
             'fields':('status','due_back')
         } )
    )

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    list_filter = ['author','title']
    inlines = (BookInstanceInlines,)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

@admin.register(Languege)
class LanguageAdmin(admin.ModelAdmin):
    pass


# inlines 


