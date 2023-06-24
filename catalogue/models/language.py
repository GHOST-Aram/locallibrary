from django.db import models
    
class Language(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='Enter books Natural Language eg(Japanese, English)'
    )

    def __str__(self):
        return self.name