from django.shortcuts import render

# Create your views here.


def basket(request):
    """
    A view for the basket.
    """

    return render(request, 'checkout/basket.html')


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