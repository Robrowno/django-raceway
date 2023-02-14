from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Contact
from trackdays.models import Trackday
from django.contrib import messages
from django.contrib.auth.decorators import login_required


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
        # create instance of the contact model
        contact = Contact()
        contact.full_name = request.POST.get('fname')
        contact.email = request.POST.get('email')
        contact.query_type = request.POST.get('query')
        contact.message = request.POST.get('textarea')
        # save to the database
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

@login_required
def management_page(request):
    """
    View to render the management page.
    """

    if request.user.is_superuser:

        if request.method == 'POST':
            new_trackday = Trackday(layout_image=request.FILES)
            new_trackday.layout = request.POST.get('td-layout')
            new_trackday.layout_image = request.POST.get('td-image')
            new_trackday.date = request.POST.get('td-date')
            new_trackday.db_limit = request.POST.get('db-limit')
            new_trackday.availability = request.POST.get('numbers')
            new_trackday.base_trackday_price = request.POST.get('base-price')
            new_trackday.save()
            messages.success(request, 'New Trackday Added')
            return redirect('trackdays')
        else:
            new_trackday = Trackday(layout_image=request.FILES)


    return render(request, 'home/management.html')


def newsletter_signup(request):
    """
    View for the Newsletter signup page. 
    """
    return render(request, 'home/newsletter.html')


def page_not_found(request,exception=None):
    """
    Custom 404 view.
    """
    return render(request,'home/error404.html',status=404)