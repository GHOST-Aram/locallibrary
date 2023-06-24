from django.shortcuts import render
from .models.author_models import Author
from .models.book_models import Book
from .models.bookInstance_models import BookInstance
from .models.genre_models import Genre
from .utils.database import Database

def index(request):
    lib_database = Database()

    authors = lib_database.retrieve_all(Author)
    num_of_authors = lib_database.count_all(authors)
    
    books = lib_database.retrieve_all(Book)
    num_of_books = lib_database.count_all(books)

    book_instances = lib_database.retrieve_all(BookInstance)
    num_of_instances = lib_database.count_all(book_instances)

    availabe_instances = BookInstance.filter_data_by_status('a')
    num_instances_available = lib_database.count_all(availabe_instances)

    genres = lib_database.retrieve_all(Genre)
    num_of_genres = lib_database.count_all(genres)

    context = {
        'num_of_authors': num_of_authors,
        'num_of_books': num_of_books,
        'num_of_instances': num_of_instances,
        'num_instances_available': num_instances_available,
        'num_of_genres': num_of_genres,
        'page_title': 'Local Library | Home',
    }

    return render(request, 'index.html', context=context)