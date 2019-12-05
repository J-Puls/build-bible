from django.shortcuts import render, redirect
from .models import Post
from .forms import FindVehicleForm, SearchForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from django.db.models import Q

def home(request):
    context = {
        'posts': Post.objects.all()[:10],
        'f_form': FindVehicleForm(),
        's_form': SearchForm(),
    }
    f_form = context['f_form']
    s_form = context['s_form']
    if f_form.is_valid():
        chosen_vehicle = f_form.vehicle
        return redirect('vehicle', chosen_vehicle)
    if s_form.is_valid():
        q = s_form.cleaned_data
        return redirect('search', q)
    return render(request, 'content/home.html', context)


class PostDetailView(DetailView):
    model = Post
    
         
class SearchListView(ListView):
    model = Post
    template_name = 'content/search_results.html'

    def get_queryset(self): 
        query = self.request.GET.get('query')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__icontains=query)
        )
        return object_list
    

def general_knowledge(request):
    return render(request, 'content/general_knowledge.html')


def faq(request):
    return render(request, 'content/faq.html')