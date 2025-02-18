from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Cat, Breed
from django.urls import reverse_lazy

class CatList(LoginRequiredMixin, ListView):
    model = Cat
    template_name = 'cats/cat_list.html'

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = ['nickname', 'weight', 'foods', 'breed']
    template_name = 'cats/cat_form.html'
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = ['nickname', 'weight', 'foods', 'breed']
    template_name = 'cats/cat_form.html'
    success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    template_name = 'cats/cat_confirm_delete.html'
    success_url = reverse_lazy('cats:all')
    
class BreedListView(LoginRequiredMixin, ListView):
    model = Breed
    template_name = 'cats/breed_list.html' 
    success_url = reverse_lazy('cats:all') 

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = ['name']
    template_name = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:all')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = ['name']
    template_name = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:all')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    template_name = 'cats/breed_confirm_delete.html'
    success_url = reverse_lazy('cats:all')
