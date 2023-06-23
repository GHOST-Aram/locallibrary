from django.db import models
from django.contrib import admin
import uuid


class BookInstance(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        help_text="Unique ID For this particular books across whole Library",
    )
    book = models.ForeignKey("Book", on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ("m", "Maintenance"),
        ("o", "On loan"),
        ("a", "available"),
        ("r", "reserved"),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        default="m",
        help_text="Book Availability",
    )

    class Meta:
        ordering = ["due_back"]

    def __str__(self):
        return f"{self.id}: {self.book.title}"

    def display_title(self):
        return self.book.title

    def display_id(self):
        return self.id

    display_title.short_description = "Title"
    display_id.short_description = "Unique Id"


class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ("display_id", "display_title", "status")
    list_filter = ("status", "due_back")
    exclude = ["id"]
    fieldsets = (
        ("Book Info", {"fields": ("book", "imprint")}),
        ("Availability", {"fields": ("status", "due_back")}),
    )
