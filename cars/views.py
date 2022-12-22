from django.shortcuts import render
from .models import Cars

# Create your views here.


def car_hire(request):
    """
    View to render the Cars/Car hire page
    """
    cars = Cars.objects.all()

    context = {
         "cars": cars,
    }

    return render(request, 'cars/car-hire.html', context)
