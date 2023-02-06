from decimal import Decimal
from django.conf import settings


def basket_contents(request):

    """
    Context Processor for use across whole site.
    Used for adding and counting products in the bag.
    """

    basket_contents = []
    total = 0
    product_count = 0
    basket = request.session.get('basket', {})

    for trackday, quantity in basket.items():
        trackday = get_object_or_404(Trackday, pk=trackday_id)
        total += quantity * trackday.price
        product_count += quantity
        basket_contents.append({
            'trackday_id': trackday_id,
            'quantity': quantity,
            'trackday': trackday,
        })

    for experience, quantity in basket.items():
        experience = get_object_or_404(experience, pk=experience_id)
        total += quantity * experience.price
        product_count += quantity
        basket_contents.append({
            'experience_id': experience_id,
            'quantity': quantity,
            'experience': experience,
        })

    for tuition, quantity in basket.items():
        tuition = get_object_or_404(Tuition, pk=tuition_id)
        total += quantity * tuition.price
        product_count += quantity
        basket_contents.append({
            'tuition_id': tuition_id,
            'quantity': quantity,
            'tuition': tuition,
        })

    context = {
        'basket_contents': basket_contents,
        'total': total,
        'product_count': product_count
    }

    return context
