from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import(
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView
)
from .forms import CinemaForm      #function based views
from .models import Cinema

class CinemaCreateView(CreateView):
    template_name = 'cinema/cinema_create.html'
    form_class = CinemaForm

class CinemaListView(ListView):
    template_name = 'cinema/cinema_list.html'
    
    def get_queryset(self):
        return Cinema.objects.all()

    def get_queryset_list(self, request):
        query = request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(title__icontains=query)
        
def get_paginator(self, request):
    paginator = Paginator(10, queryset) # Show 25 contacts per page
    page = request.GET.get('page')
    queryset = paginator.get_page(page)
    return render(request, 'cinema/cinema_list.html', {'queryset': queryset})

class CinemaDetailView(DetailView):
    template_name = 'cinema/cinema_detail.html'
    form_class = CinemaForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Cinema, id=id_)

class CinemaUpdateView(UpdateView):
    template_name = 'cinema/cinema_create.html'
    form_class = CinemaForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Cinema, id=id_)

class CinemaDeleteView(DeleteView):
    template_name = 'cinema/cinema_delete.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Cinema, id=id_)
    def get_success_url(self):
        return reverse('cinema:cinema-list')