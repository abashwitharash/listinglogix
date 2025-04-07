from django.shortcuts import render


class Property:
    def __init__(self, address, price, status, description):
        self.address = address
        self.price = price
        self.status = status
        self.description = description

# Define the home view function
def home(request):
    # Send a simple HTML response
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def lists_index(request):
    # Render the cats/index.html template with the cats data
    return render(request, 'lists/index.html', {'property': property})
