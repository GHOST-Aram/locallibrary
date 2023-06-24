class Database:
    def count_all(self, queryset):
        return queryset.count()

    def retrieve_all(self, model):
        return model.objects.all()

    def insert_data(new_data_instance):
        new_data_instance.save()

    def update_data(updated_model_instance):
        updated_model_instance.save()

