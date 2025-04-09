from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Property

class ListCreate(LoginRequiredMixin, CreateView):
    model = Property
    fields = '__all__'

def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

class ListUpdate(LoginRequiredMixin, UpdateView):
    model = Property
    fields = ['price', 'status', 'details', 'dom']

class ListDelete(LoginRequiredMixin, DeleteView):
    model = Property
    success_url = '/lists/'

# Define the home view function
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

@login_required
def lists_index(request):
    properties = Property.objects.filter(user=request.user)
    return render(request, 'lists/index.html', {'properties': properties})

@login_required
def list_detail(request, list_id):
    property = Property.objects.get(id=list_id)
    return render(request, 'lists/detail.html', {'property': property})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('lists-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)

def all_listings(request):
    properties = Property.objects.all()
    return render(request, 'lists/all.html', {'properties': properties})