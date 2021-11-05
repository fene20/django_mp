from decimal import Decimal
from django.conf import settings

def bag_contents(request):

    bag_items = []
    total = 0.0
    product_count = 0
    discount = 0.0

    # 2 options here. A discount if more than 1 item is purchased or a discount if the cost is over a certain value
    # A coustomer will likely order just one graphic so will go with the first option.
    if product_count < 2:
        discount = 0.0
        grand_total = total
    else:
        discount = total * settings.DISCOUNT_PERCENTAGE
        grand_total = total - discount

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'discount': discount,
        'discount_percentage': settings.DISCOUNT_PERCENTAGE,
        'grand_total': grand_total,
    }

    return context
