from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import sentimentForm

# Create your views here.


def index(request):
    '''
    View Function to display the main page
    '''
    template = loader.get_template('myApp/index.html')
    return render(request, 'myApp/index.html')

def get_sentiment(request):
    '''
    View Function to handle a user's input through a form
    '''
    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form = sentimentForm(request.POST)
        #Check whether it's valid:
        if form.is_valid():
            your_sentiment = form.cleaned_data['your_sentiment']
        else:
            form = sentimentForm()
        return render(request, 'myApp/index.html', {'form': form})

