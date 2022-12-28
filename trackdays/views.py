from django.shortcuts import render, get_object_or_404
from .models import Experiences

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

    experiences = Experiences.objects.all()

    context = {
        "experiences": experiences,
    }

    return render(request, 'trackdays/experiences.html', context)


def experiences_detail(request, pk):
    """
    View to render the experiences detail page.
    """
    experiences = Experiences.objects.get(id=pk)

    context = {
        "experiences": experiences,
    }

    return render(request, 'trackdays/experience-detail.html', context)
