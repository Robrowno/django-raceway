from django.shortcuts import render

# Create your views here.


def home_page(request):
    """
    View to render the Home Page.
    """

    return render(request, 'home/index.html')


def contact_page(request):
    """
    View to render the Contact Page.
    """

    return render(request, 'home/contact.html')


def about_page(request):
    """
    View to render the About Page.
    """

    return render(request, 'home/about.html')
