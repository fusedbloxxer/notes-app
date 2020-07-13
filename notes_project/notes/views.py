from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from notes.forms import NotesForm
from django.urls import reverse
from notes.models import Note


class ListNoteView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes_list.html'
    context_object_name = 'notes_list'
    login_url = '/auth/accounts/login/'

    def get_queryset(self):
        return Note.objects.order_by('add_date')


class DetailNoteView(LoginRequiredMixin, DetailView):
    model = Note
    template_name = 'notes_detail.html'
    login_url = '/auth/accounts/login/'


class CreateNoteView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NotesForm
    template_name = 'notes_form.html'
    login_url = '/auth/accounts/login/'

    def get_success_url(self):
        return reverse('notes:list')


class UpdateNoteView(LoginRequiredMixin, UpdateView):
    model = Note
    form_class = NotesForm
    template_name = 'notes_form.html'
    login_url = '/auth/accounts/login/'

    def get_success_url(self):
        return reverse('notes:list')


class DeleteNoteView(LoginRequiredMixin, DeleteView):
    model = Note
    template_name = 'notes_delete.html'
    login_url = '/auth/accounts/login/'

    def get_success_url(self):
        return reverse('notes:list')


def index(request):
    return redirect('home')


def home(request):
    return render(request, 'home.html')
