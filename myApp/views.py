from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


def index(request):
    '''
    View Function to display the main page
    '''
    template = loader.get_template('myApp/index.html')
    return render(request, 'myApp/index.html')

