from django.shortcuts import render
from .models.author_models import Author
from .models.book_models import Book
from .models.bookInstance_models import BookInstance
from .utils.database import Database

def index(request):
    database = Database()

    num_of_authors = database.count_all(Author)
    num_of_books = database.count_all(Book)
    num_of_instances = database.count_all(BookInstance)
    num_instances_available = database.count_all_by_status_exact(BookInstance, 'a')

    context = {
        'num_of_authors': num_of_authors,
        'num_of_books': num_of_books,
        'num_of_instances': num_of_instances,
        'num_instances_available': num_instances_available,
    }

    return render(request, 'index.html', context=context)