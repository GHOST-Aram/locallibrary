from django.contrib import admin
from django.db import models
from .genre import Genre
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        max_length=1000, help_text="Enter a brief desciption of the book"
    )
    isbn = models.CharField(
        "ISBN",
        max_length=13,
        unique=True,
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">'
        + "ISBN number</a>",
    )
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book.")
    language = models.ForeignKey("Language", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.title}"

    def display_genre(self):
        return ", ".join(genre.name for genre in self.genre.all()[:2])

    display_genre.short_description = "Genre"

    def exclude_by_title(exlude_title):
        return Book.objects.all().exclude(title__icontains=exlude_title)

    def filter_by_matching_title(text_match):
        return Book.objects.filter(title__icontains=text_match)
    
    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])


class BookAdmin(admin.ModelAdmin):
    list_display = ("isbn", "__str__", "author", "display_genre")
    empty_value_display = "Unknown"
    list_filter = ["author", "language"]
    fields = [("title", "author", "isbn"), "summary", ("genre", "language")]
