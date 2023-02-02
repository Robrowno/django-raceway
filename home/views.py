from django.shortcuts import render

# Create your views here.


def home_page(request):
    """
    View to render the Home Page.
    """

    return render(request, 'home/index.html')
