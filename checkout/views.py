from django.shortcuts import render, redirect, get_object_or_404
from trackdays.models import Tuition, Experiences

# Create your views here.


def basket(request):
    """
    A view for the basket.
    """

    return render(request, 'checkout/basket.html')


def add_exp_to_basket(request, experience_id):
    """
    For adding an experience package to the basket.
    """
    # experience = Experiences.objects.get(pk=experience_id)
    experience = get_object_or_404(Experiences, pk=experience_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {'experience': {}, 'tuition': {}, 'trackday': {}})

    if experience_id in list(basket.keys()):
        if experience_id in list(basket.keys()):
            basket['experience'][experience_id] += quantity
    else:
        basket['experience'][experience_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)


def add_tuition_to_basket(request, tuition_id):
    """
    For adding a tuition course to the basket.
    """
    tuition = Tuition.objects.get(pk=tuition_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {'experience': {}, 'tuition': {}, 'trackday': {}})

    if tuition_id in list(basket.keys()):
        if tuition_id in list(basket.keys()):
            basket['tuition'][tuition_id] += quantity
    else:
        basket['tuition'][tuition_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)


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
