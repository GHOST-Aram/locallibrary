from django.shortcuts import render
from django.views import generic
from .models.author import Author
from .models.book import Book
from .models.bookInstance import BookInstance
from .models.genre import Genre
from .utils.table import Table

def index(request):
    lib_table = Table()

    authors = lib_table.retrieve_all(Author)
    num_of_authors = lib_table.count_all(authors)
    
    books = lib_table.retrieve_all(Book)
    num_of_books = lib_table.count_all(books)
    
    books_not_about_rich = Book.exclude_by_title('rich')
    num_book_not_on_rich = lib_table.count_all(books_not_about_rich)

    books_with_matching_title = Book.filter_by_matching_title('how')
    num_books_matching_how = lib_table.count_all(books_with_matching_title)

    books_order_by_title = Book.order_by_title()

    book_instances = lib_table.retrieve_all(BookInstance)
    num_of_instances = lib_table.count_all(book_instances)

    availabe_instances = BookInstance.filter_data_by_status('a')
    num_instances_available = lib_table.count_all(availabe_instances)

    genres = lib_table.retrieve_all(Genre)
    num_of_genres = lib_table.count_all(genres)


    context = {
        'num_of_authors': num_of_authors,
        'num_of_books': num_of_books,
        'num_of_instances': num_of_instances,
        'num_instances_available': num_instances_available,
        'num_of_genres': num_of_genres,
        'page_title': 'Local Library | Home',
        'titles_matching_how': num_books_matching_how,
        'not_on_money': Book.filter_by_title_end('people')[0]
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book

    # Overidding ListView Properties
    context_object_name = 'book_list'
    # queryset = Book.filter_by_matching_title('how')[:3]
    template_name = 'catalogue/book_list.html'
    paginate_by = 2
    
    def get_queryset(self):
        return Book.objects.all()
    
class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'catalogue/book_detail.html'
    extra_context ={'owner': 'Maseno University Library'}

    def get_queryset(self):
        return super().get_queryset()
    