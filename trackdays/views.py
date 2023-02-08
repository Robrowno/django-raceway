from django.shortcuts import render, get_object_or_404, redirect
from .models import (
    Experiences, Trackday, TrackdayRequest, TrackdayBooking, Tuition
    )
from django.contrib import messages

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

    if request.method == 'POST':
        trackday_req = TrackdayRequest()
        trackday_req.organiser = request.POST.get('organiser')
        trackday_req.email = request.POST.get('email')
        trackday_req.phone_number = request.POST.get('tel')
        trackday_req.date_request = request.POST.get('date')
        trackday_req.full_or_half_day = request.POST.get('fullorhalf')
        trackday_req.number_of_spaces = request.POST.get('num_spaces')
        trackday_req.hospitality = request.POST.get('hosp_req')
        trackday_req.pitlanes = request.POST.get('pitlanes')
        trackday_req.db_limit = request.POST.get('db_limit')
        trackday_req.car_hire_required = request.POST.get('carhire')
        trackday_req.save()
        messages.success(request, 'Your Track Day request was succesfully sent!')
        return redirect('home')

    else:
        trackday_req = TrackdayRequest()

    context = {
        'trackday_req': trackday_req,
    }

    return render(request, 'trackdays/trackday-request.html', context)


def tuition(request):
    """
    View to render the tuition information.
    """
    tuition = Tuition.objects.all()

    context = {
        "tuition": tuition
    }

    return render(request, 'trackdays/tuition.html', context)


def tuition_detail(request, tuition_id):
    """
    View to render the tuition details information.
    """
    tuition = get_object_or_404(Tuition, pk=tuition_id)

    context = {
        "tuition": tuition
    }

    return render(request, 'trackdays/tuition-detail.html', context)


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
