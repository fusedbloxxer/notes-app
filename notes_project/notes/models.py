from django.db import models


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=120, verbose_name='Titlu', help_text='Titlu reprezentativ')
    content = models.TextField(verbose_name='Text', help_text='Continutul notitei')
    add_date = models.DateTimeField(verbose_name='Data adaugare')
    is_complete = models.BooleanField(verbose_name='Este finalizata', default=False)
