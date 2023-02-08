from django.shortcuts import render, redirect, get_object_or_404, reverse
from trackdays.models import Tuition, Experiences
from django.contrib import messages

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
