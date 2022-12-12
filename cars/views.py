from django.shortcuts import render

# Create your views here.


def car_hire(request):
    """
    View to render the Cars/Car hire page
    """

    return render(request, 'cars/car-hire.html')
