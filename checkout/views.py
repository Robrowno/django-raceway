from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from trackdays.models import Tuition, Experiences, Trackday, TrackdayBooking
from cars.models import Cars
from django.contrib import messages


def basket(request):
    """
    A view for the basket.
    """

    return render(request, 'checkout/basket.html')

def add_trackday_to_basket(request, trackday_id):
    """
    For adding a track day order to the basket
    """
    trackday = get_object_or_404(Trackday, pk=trackday_id)
    quantity = 0
    basket = request.session.get('basket', {'experience': {}, 'tuition': {}, 'trackday': {}})

    if request.method == 'POST':
        booking = TrackdayBooking(trackday=trackday)
        booking.full_or_half_day = request.POST.get('fullHalfDay')
        booking.paddock_hire = request.POST.get('paddockhire')
        booking.additional_drivers = request.POST.get('driver-number')
        booking.helmet_hire = request.POST.get('helmet-number')
        booking.tuition = request.POST.get('tuition-number')
        booking.car_hire = get_object_or_404(Cars, id=request.POST.get('carhire'))
        booking.save()

        if trackday_id in list(basket.keys()):
            basket['trackday'][trackday_id] += quantity
        else:
            basket['trackday'][trackday_id] = quantity
        
    request.session['basket'] = basket
    return redirect('trackdays')

def remove_trackday_from_basket(request, trackday_id):
    """
    View to remove a trackday item from the basket
    """

    trackday = get_object_or_404(Trackday, pk=trackday_id)
    booking = TrackdayBooking(trackday=trackday)

    try:
        basket = request.session.get('basket', {'experience': {}, 'tuition': {}, 'trackday': {}})
        item = basket['trackday'][item_id]
        basket['trackday'].pop(item_id)
        booking.delete()

        request.session['basket'] = basket
        messages.warning(request, "Removed from the basket.")

        return HttpResponse(status=200)
        
    except Exception as e:
        print(e)
        return HttpResponse(status=500)



def add_exp_to_basket(request, experience_id):
    """
    For adding an experience package to the basket.
    """
    experience = get_object_or_404(Experiences, pk=experience_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {'experience': {}, 'tuition': {}, 'trackday': {}})

    if experience_id in list(basket.keys()):
        basket['experience'][experience_id] += quantity
    else:
        basket['experience'][experience_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)


def add_tuition_to_basket(request, tuition_id):
    """
    For adding a tuition course to the basket.
    """
    tuition = get_object_or_404(Tuition, pk=tuition_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {'experience': {}, 'tuition': {}, 'trackday': {}})

    if tuition_id in list(basket.keys()):
        basket['tuition'][tuition_id] += quantity
    else:
        basket['tuition'][tuition_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)


def edit_exp_quantity(request, item_id):
    """
    For editing experience quantities in the basket.
    """
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {'experience': {}, 'tuition': {}, 'trackday': {}})

    if quantity > 0:
        basket['experience'][item_id] = quantity
    else:
        basket.pop['experience'][item_id]

    request.session['basket'] = basket
    messages.success(request, "Basket successfully updated.")
    return redirect(reverse('my_basket'))


def remove_exp(request, item_id):
    """
    For removing an Experience item from the basket
    """

    try:
        basket = request.session.get('basket', {'experience': {}, 'tuition': {}, 'trackday': {}})
        item = basket['experience'][item_id]
        basket['experience'].pop(item_id)

        request.session['basket'] = basket
        messages.warning(request, "Removed from the basket.")
        return HttpResponse(status=200)

    except Exception as e:
        print(e)
        return HttpResponse(status=500)


def remove_tuition(request, item_id):
    """
    For removing a Tuition item from the basket
    """

    try:
        basket = request.session.get('basket', {'experience': {}, 'tuition': {}, 'trackday': {}})
        item = basket['tuition'][item_id]
        basket['tuition'].pop(item_id)

        request.session['basket'] = basket
        messages.warning(request, "Removed from the basket.")
        return HttpResponse(status=200)

    except Exception as e:
        print(e)
        return HttpResponse(status=500)


def edit_tuition_quantity(request, item_id):
    """
    For editing tuition quantities in the basket.
    """
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {'experience': {}, 'tuition': {}, 'trackday': {}})

    if quantity > 0:
        basket['tuition'][item_id] = quantity
    else:
        basket.pop['tuition'][item_id]

    request.session['basket'] = basket
    messages.success(request, "Basket successfully updated.")
    return redirect(reverse('my_basket'))


def checkout(request):
    """
    A view for the checkout page
    """

    return render(request, 'checkout/checkout.html')


def checkout_success(request):
    """
    A view for the checkout success page
    """

    return render(request, 'checkout/checkout_success.html')
