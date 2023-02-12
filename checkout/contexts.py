from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from trackdays.models import Trackday, TrackdayBooking, Tuition, Experiences


grand_total = 0


def basket_contents(request):
    """
    Context Processor for use across whole site.
    Used for adding and counting products in the bag.
    """

    basket_contents = []
    total = 0
    product_count = 0
    trackday_price = 0
    basket = request.session.get(
        'basket', {'experience': {}, 'tuition': {}, 'trackday': {}}
    )

    if 'trackday' in basket:
        for trackday, quantity in basket['trackday'].items():
            # gets trackday by primary key
            trackday = get_object_or_404(Trackday, pk=trackday)
            # gets the relational booking by trackday
            booking = TrackdayBooking.objects.filter(
                trackday=trackday, user=request.user)
            # iterating through the trackday booking options
            for item in booking:
                if item.full_or_half_day == 1:
                    # full day
                    base_price = item.trackday.base_trackday_price
                else:
                    # half day
                    base_price = item.trackday.base_trackday_price // 2
                carhire = item.car_hire.cost_to_hire
                # multiplying quantities by fixed prices
                additional_drivers = item.additional_drivers * 10
                helmet_hire = item.helmet_hire * 10
                tuition_cost = item.tuition * 25
                paddock = item.paddock_hire
                # add up the cost of all the options
                trackday_price = (
                    base_price +
                    carhire +
                    additional_drivers +
                    helmet_hire +
                    tuition_cost +
                    paddock)

            # trackday quantity is always 1
            quantity = 1
            # increase total by adding on trackday price
            total += trackday_price
            # increase product count by 1
            product_count += quantity
            basket_contents.append({
                'trackday': trackday,
                'quantity': quantity,
            })
            

    if 'experience' in basket:
        for experience, quantity in basket['experience'].items():
            experience = get_object_or_404(Experiences, pk=experience)
            total += quantity * experience.price
            product_count += quantity
            basket_contents.append({
                'quantity': quantity,
                'experience': experience,
            })

    if 'tuition' in basket:
        for tuition, quantity in basket['tuition'].items():
            tuition = get_object_or_404(Tuition, pk=tuition)
            total += quantity * tuition.price
            product_count += quantity
            basket_contents.append({
                'tuition': tuition,
                'quantity': quantity,
            })
    
    context = {
        'basket_contents': basket_contents,
        'total': total,
        'product_count': product_count,
        'grand_total': calc_vat(request, total),
        'trackday_price': trackday_price,
    }

    return context


def calc_vat(request, total):
    """
    Calculates the total cost including VAT at 20%
    """
    vat_rate = Decimal('0.20')
    vat_amount = total * vat_rate
    grand_total = total + vat_amount

    return grand_total
