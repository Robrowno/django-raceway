from django.shortcuts import render

# Create your views here.


def track_day_list(request):
    """
    View to render the Track day list menu.
    """

    return render(request, 'trackdays/trackday-list.html')


def track_day_detail(request):
    """
    View to render the Track day detail booking page.
    """

    return render(request, 'trackdays/trackday-detail.html')


def track_day_request(request):
    """
    View to render the track day request page.
    """

    return render(request, 'trackdays/trackday-request.html')


def tuition(request):
    """
    View to render the tuition information.
    """

    return render(request, 'trackdays/tuition.html')

    
def experiences(request):
    """
    View to render the experiences information.
    """

    return render(request, 'trackdays/experiences.html')


def experiences_detail(request):
    """
    View to render the experiences detail page.
    """

    return render(request, 'trackdays/experience-detail.html')
