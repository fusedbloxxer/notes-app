from django.db import models


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=120, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    add_date = models.DateTimeField(verbose_name='Add Date')
    is_complete = models.BooleanField(verbose_name='It\'s Done', default=False)
