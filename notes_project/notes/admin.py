from django.contrib import admin

# Register your models here.
from notes.models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'add_date', 'is_complete']


admin.site.register(Note, NoteAdmin)
