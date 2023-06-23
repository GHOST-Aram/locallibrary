from django.db import models
from django.contrib import admin

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ['first_name', 'last_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(id)])
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date_of_birth', 'date_of_death_view')
    fields = [('first_name', 'last_name'), ('date_of_birth', 'date_of_death')]

    @admin.display(empty_value='Date unknown')
    def date_of_death_view(self, author):
        return author.date_of_death
