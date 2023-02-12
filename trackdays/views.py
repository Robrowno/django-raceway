from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import (
    Experiences, Trackday, TrackdayRequest, TrackdayBooking, Tuition
    )
from cars.models import Cars
from django.contrib import messages
from checkout.contexts import basket_contents

trackDayID=0
def is_availability(trackday_id):
    trackday = Trackday.objects.get(id=trackday_id)
    if trackday.availability >=0:
        return True
    else:
        return False
def track_day_list(request):
    """
    View to render the Track day list menu.
    """
    basket = request.session.get(
        'basket', {'experience': {}, 'tuition': {}, 'trackday': {}})
    trackday_list = Trackday.objects.all()
    basket_trackdays = [x for x in basket['trackday'].keys()]
    available_tracks = [x for x in trackday_list if str(x.id) not in basket_trackdays]
    isExist=False
    isAvailable=[]
    trackdays = Trackday.objects.all()
    for trackday in trackdays:
        trackday_data = {
            "trackday_id": trackday.id,
            "availability": is_availability(trackday.id)
        }
        isAvailable.append(trackday_data)
    print(isAvailable)
    if len(basket_trackdays) >0:
        isExist=True
    context = {
        "trackdays": available_tracks,
        "flag":isExist,
        "available":isAvailable
    }

    return render(request, 'trackdays/trackday-list.html', context)


@login_required
def track_day_detail(request, trackday_id):
    """
    View to render the Track day detail booking page.
    """
    trackday = get_object_or_404(Trackday, pk=trackday_id)
    cars = Cars.objects.all()

    context = {
        "trackday": trackday,
        "cars": cars,
    }

    return render(request, 'trackdays/trackday-detail.html', context)


def track_day_request(request):
    """
    View to render the track day request page.
    """

    if request.method == 'POST':
        # create instance of the trackday request model
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
        # save the information to the database
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
