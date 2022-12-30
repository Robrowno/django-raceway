from django.shortcuts import render, get_object_or_404
from .models import Experiences, Trackday, TrackdayBooking

# Create your views here.


def track_day_list(request):
    """
    View to render the Track day list menu.
    """
    trackday_list = Trackday.objects.all()

    context = {
        "trackdays": trackday_list,
    }

    return render(request, 'trackdays/trackday-list.html', context)


def track_day_detail(request, trackday_id):
    """
    View to render the Track day detail booking page.
    """
    trackday = get_object_or_404(Trackday, pk=trackday_id)

    context = {
        "trackday": trackday,
    }

    return render(request, 'trackdays/trackday-detail.html', context)


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


def experiences_detail(request, experience_id):
    """
    View to render the experiences detail page.
    """
    experience = get_object_or_404(Experiences, pk=experience_id)

    context = {
        "experience": experience,
    }

    return render(request, 'trackdays/experience-detail.html', context)
