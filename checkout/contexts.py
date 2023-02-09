from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from trackdays.models import Trackday, Tuition, Experiences


grand_total = 0

def basket_contents(request):

    """
    Context Processor for use across whole site.
    Used for adding and counting products in the bag.
    """

    basket_contents = []
    total = 0
    product_count = 0
    basket = request.session.get(
        'basket', {'experience': {}, 'tuition': {}, 'trackday': {}}
        )

    if 'trackday' in basket:
        for trackday, quantity in basket['trackday'].items():
            trackday = get_object_or_404(Trackday, pk=trackday)
            total += quantity * trackday.price
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

    print(calc_vat(request, total))
    context = {
        'basket_contents': basket_contents,
        'total': total,
        'product_count': product_count,
        'grand_total': calc_vat(request, total),
    }

    return context


def calc_vat(request, total):

    """
    For calculating the total cost including VAT
    """
    vat_rate = Decimal('0.20')
    vat_amount = total * vat_rate
    grand_total = total + vat_amount

    return grand_total