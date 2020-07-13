from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from notes.forms import NotesForm
from django.urls import reverse
from notes.models import Note


class ListNoteView(ListView):
    model = Note
    template_name = 'notes_list.html'
    context_object_name = 'notes_list'

    def get_queryset(self):
        return Note.objects.order_by('add_date')


class DetailNoteView(DetailView):
    model = Note
    template_name = 'notes_detail.html'


class CreateNoteView(CreateView):
    model = Note
    form_class = NotesForm
    template_name = 'notes_form.html'

    def get_success_url(self):
        return reverse('notes:list')


class UpdateNoteView(UpdateView):
    model = Note
    form_class = NotesForm
    template_name = 'notes_form.html'

    def get_success_url(self):
        return reverse('notes:list')


class DeleteNoteView(DeleteView):
    model = Note
    template_name = 'notes_delete.html'

    def get_success_url(self):
        return reverse('notes:list')


def index(request):
    return redirect('notes:list')
