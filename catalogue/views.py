from django.shortcuts import render
from .models.author import Author
from .models.book import Book
from .models.bookInstance import BookInstance
from .models.genre import Genre
from .utils.database import Database

def index(request):
    lib_database = Database()

    authors = lib_database.retrieve_all(Author)
    num_of_authors = lib_database.count_all(authors)
    
    books = lib_database.retrieve_all(Book)
    num_of_books = lib_database.count_all(books)
    
    books_not_about_rich = Book.exclude_by_title('rich')
    num_book_not_on_rich = lib_database.count_all(books_not_about_rich)

    books_with_matching_title = Book.filter_by_matching_title('how')
    num_books_matching_how = lib_database.count_all(books_with_matching_title)

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
        'titles_matching_how': num_books_matching_how,
        'not_on_money': num_book_not_on_rich
    }

    return render(request, 'index.html', context=context)