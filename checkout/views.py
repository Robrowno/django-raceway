from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from django.contrib.auth.models import User
from trackdays.models import Tuition, Experiences, Trackday, TrackdayBooking
from cars.models import Cars
from django.contrib import messages
import stripe
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect
from checkout.contexts import basket_contents
from django.conf import settings
from checkout.models import OrderItem
from profiles.models import UserProfile
stripe.api_key=settings.API_KEY

trackDayID=0

def basket(request):
    """
    A view for the basket.
    """

    return render(request, 'checkout/basket.html')

def error(request):
    """
    A view for the error.
    """

    return render(request, 'error.html')

def decrement_availability(trackday_id):
    trackday = Trackday.objects.get(id=trackday_id)
    if trackday.availability > 0:
        trackday.availability -= 1
        trackday.save()
        return True
    else:
        return False


def success(request):
    # print(request.session)
    if 'session_id' in request.session:
        session_id = request.session.pop('session_id')
        session = stripe.checkout.Session.retrieve(session_id)
        sessions = stripe.checkout.Session.retrieve(session_id,expand=['line_items'],)
        payment_intent = stripe.PaymentIntent.retrieve(session["payment_intent"])
        # print("sessions.status=>",session.status)
        if session.status == 'complete':
            recipient_url = payment_intent['charges']['data'][0]['receipt_url']
            pid=basket_contents(request)['pid']
            profile=UserProfile.objects.get(id=pid)
            order=OrderItem(user_profile=profile,stripe_reciept=recipient_url)
            order.save()
            if 'trackday' in request.session:
                decrement_availability(trackDayID)
            if 'basket' in request.session:
                del request.session['basket']
            else:
                return redirect('/')
            return render(request, "success.html")
        else:
            return render(request,"error.html")
def cancel(request):
    """
    A view for the basket.
    """

    return render(request, 'cancel.html')
def add_trackday_to_basket(request, trackday_id):
    """
    For adding a track day order to the basket
    """
    trackday = get_object_or_404(Trackday, pk=trackday_id)
    quantity = 0
    basket = request.session.get(
        'basket', {'experience': {}, 'tuition': {}, 'trackday': {}})

    if request.method == 'POST':
        # instance of the trackday booking model
        booking = TrackdayBooking(trackday=trackday, user=request.user)
        booking.full_or_half_day = request.POST.get('fullHalfDay')
        booking.paddock_hire = request.POST.get('paddockhire')
        booking.additional_drivers = request.POST.get('driver-number')
        booking.helmet_hire = request.POST.get('helmet-number')
        booking.tuition = request.POST.get('tuition-number')
        # get the car object if selected in the options
        booking.car_hire = get_object_or_404(
            Cars, id=request.POST.get('carhire'))
        # save the booking
        booking.save()
        quantity = 1

        if trackday_id in list(basket.keys()):
            basket['trackday'][trackday_id] += quantity
        else:
            basket['trackday'][trackday_id] = quantity

    request.session['basket'] = basket
    return redirect('trackdays')


def remove_trackday_from_basket(request, item_id):
    """
    View to remove a trackday item from the basket
    """
    # Access the specific trackday product
    trackday = get_object_or_404(Trackday, pk=item_id)
    # Access the specific booking
    booking = TrackdayBooking.objects.get(trackday=trackday, user=request.user)

    try:
        basket = request.session.get(
            'basket', {'experience': {}, 'tuition': {}, 'trackday': {}})
        item = basket['trackday'][item_id]
        # remove the trackday from the basket
        basket['trackday'].pop(item_id)
        # delete the booking from the database
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
    basket = request.session.get(
        'basket', {'experience': {}, 'tuition': {}, 'trackday': {}})

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
    basket = request.session.get(
        'basket', {'experience': {}, 'tuition': {}, 'trackday': {}})

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
    basket = request.session.get(
        'basket', {'experience': {}, 'tuition': {}, 'trackday': {}})

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
        basket = request.session.get(
            'basket', {'experience': {}, 'tuition': {}, 'trackday': {}})
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
        basket = request.session.get(
            'basket', {'experience': {}, 'tuition': {}, 'trackday': {}})
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
    basket = request.session.get(
        'basket', {'experience': {}, 'tuition': {}, 'trackday': {}})

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
    # print(request.user.id)
    current_url=request.build_absolute_uri()
    base_url=current_url.split("/")[0] + "//" + current_url.split("/")[2]
    # print(base_url)
    products = {
        'image':[],
    }
    data = basket_contents(request)
    basket_content=data['basket_contents']
    grand_total=data['grand_total']
    grand_total=int(grand_total)
    if len(basket_content)>0:
        for item in basket_content:
            if "trackday" in item:
                global trackDayID
                trackDayID=item['trackday'].id
                trackday_obj = item['trackday']
                image=trackday_obj.layout_image
                products['image'].append(image.url)
            if "tuition" in item:
                # print("tuition" in basket_content)
                tuition_obj = item['tuition']
                image=tuition_obj.small_image
                products['image'].append(image.url)
            if "experience" in item:
                experience_obj = item['experience']
                image=experience_obj.image
                products['image'].append(image.url)  
        full_urls = [base_url + image for image in products['image']]
        session=stripe.checkout.Session.create(
        success_url=base_url+"/checkout/success",
        cancel_url=base_url+"/checkout/cancel",
        line_items=[
            {
            "price_data": {
                "currency":"GBP",
                "product_data":{
                    "name":"All cart products",
                    'images':full_urls,
                },
                "unit_amount":grand_total*100
            },
            "quantity": 1,
            },
        ],
        mode="payment",
        )
        request.session['session_id'] = session['id']
        # print(session.url)
        # print(session['id']=='cs_test_a1a5Wf5glehWfK0M2sCBy0ONbIhG3ZokJ9WKWYNSnf5GpUaJU8lVh1MSP5')
        sessions = stripe.checkout.Session.retrieve('cs_test_a1a5Wf5glehWfK0M2sCBy0ONbIhG3ZokJ9WKWYNSnf5GpUaJU8lVh1MSP5',expand=['line_items'],)
        # print(sessions)
        # print("AFTER")
        return HttpResponseRedirect(session.url)
    else:
        messages.error(request, "Your basket is empty. Please add products to your basket.")
        return redirect('/')
