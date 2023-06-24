class Database:
    def count_all(self, queryset):
        return queryset.count()

    def retrieve_all(self, entry):
        return entry.objects.all()

    def insert_data(new_entry):
        new_entry.save()

    def update_data(updated_entry):
        updated_entry.save()

