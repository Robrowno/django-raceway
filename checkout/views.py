from django.shortcuts import render, redirect

# Create your views here.


def basket(request):
    """
    A view for the basket.
    """

    return render(request, 'checkout/basket.html')


def add_exp_to_basket(request):
    """
    For adding an experience package to the basket.
    """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if experience_id in list(basket.keys()):
        if experience_id in list(bag.keys()):
            basket[experience_id] += quantity
    else:
        basket[experience_id] = quantity

    request.session['basket'] = basket
    print(request.session['basket'])
    return redirect(redirect_url)


def add_tuition_to_basket(request):
    """
    For adding a tuition course to the basket.
    """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if tuition_id in list(basket.keys()):
        if tuition_id in list(bag.keys()):
            basket[tuition_id] += quantity
    else:
        basket[tuition_id] = quantity

    request.session['basket'] = basket

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