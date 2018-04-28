from django.shortcuts import render, render_to_response
from django.template import loader
from django.http import HttpResponse
from .models import Note
from django.views import generic
from .forms import NoteForm 

# Create your views here.
class IndexView(generic.ListView):
   model = Note  
   template_name = 'notes/index.html'
   
   def get_queryset(self):
    notes = Note.objects
    return notes; 

def home(request):
    notes = Note.objects
    template = loader.get_template('index.html')
    form = NoteForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save() 
    context = {'notes': notes,'form': form}
    return render(request, 'index.html', context) 
