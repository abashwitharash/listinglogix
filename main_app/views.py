from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Property

class ListCreate(CreateView):
    model = Property
    fields = '__all__'

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def lists_index(request):
    properties = Property.objects.all()
    return render(request, 'lists/index.html', {'properties': properties})

def list_detail(request, list_id):
    property = Property.objects.get(id=list_id)
    return render(request, 'lists/detail.html', {'property': property})
