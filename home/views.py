from django.shortcuts import render, HttpResponseRedirect
from .models import Contact
from django.contrib import messages

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

    submitted = False
    if request.method == 'POST':
        contact = Contact()
        contact.first_name = request.POST.get('fname')
        contact.last_name = request.POST.get('lname')
        contact.email_address = request.POST.get('email')
        contact.query_type = request.POST.get('query')
        contact.textbox = request.POST.get('textarea')
        contact.save()
        messages.success(request, 'Your Message was sent!')
        return HttpResponseRedirect('/contact?submitted=True')

    else:
        contact = Contact()
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'contact': contact,
        'submitted': submitted
    }

    return render(request, 'home/contact.html', context)


def about_page(request):
    """
    View to render the About Page.
    """

    return render(request, 'home/about.html')


def faqs_page(request):
    """
    View to render the FAQs page.
    """

    return render(request, 'home/faqs.html')


def policies_page(request):
    """
    View to render the policies page.
    """

    return render(request, 'home/policies.html')
