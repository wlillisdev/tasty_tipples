from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def about(request):
    """ Displays about us page """
    return render(request, 'home/about.html')


def privacy(request):
    """ Displays privacy poilcy """
    return render(request, 'home/privacy.html')
