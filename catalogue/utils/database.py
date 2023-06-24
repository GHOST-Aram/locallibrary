class Database:

    def get_all(self, model):
        return model.objects.all()

    def count_all(self, model):
        return self.get_all(model).count()
    
    def filter_by_status_exact(self, model, status):
        return model.objects.filter(status__exact=status)
    
    def count_all_by_status_exact(self, model, status):
        return self.filter_by_status_exact(model, status).count()