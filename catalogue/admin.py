from django.contrib import admin
from .models.author_models import Author, AuthorAdmin
from .models.book_models import Book, BookAdmin
from .models.bookInstance_models import BookInstance, BookInstanceAdmin
from .models.genre_models import Genre
from .models.language_models import Language

admin.site.register(Author, AuthorAdmin)   
admin.site.register(Book, BookAdmin)
admin.site.register(BookInstance, BookInstanceAdmin)
admin.site.register(Genre)
admin.site.register(Language)