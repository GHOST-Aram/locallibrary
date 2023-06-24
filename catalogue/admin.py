from django.contrib import admin
from .models.author import Author, AuthorAdmin
from .models.book import Book, BookAdmin
from .models.bookInstance import BookInstance, BookInstanceAdmin
from .models.genre import Genre
from .models.language import Language

admin.site.register(Author, AuthorAdmin)   
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)
admin.site.register(Language)