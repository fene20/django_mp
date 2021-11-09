from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from graphics.models import Graphic

def bag_contents(request):

    bag_items = []
    graphic_count = 0
    discount = 0.0
    total = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        # if item has no sizes, i.e. item_data is an integer
        if isinstance(item_data, int):
            graphic = get_object_or_404(Graphic, pk=item_id)
            total += item_data * graphic.price
            graphic_count += item_data
            bag_items.append({
                'item_id': item_id,
                'quantity': item_data,
                'graphic': graphic,
            })
        else:
            # is a dictionary, see size added to bag_items
            graphic = get_object_or_404(Graphic, pk=item_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * graphic.price
                graphic_count += quantity
                bag_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'graphic': graphic,
                    'size': size,
                })

    # 2 options here. A discount if more than 1 item is purchased or a discount if the cost is over a certain value
    # A coustomer will likely order just one graphic so will go with the first option.
    if graphic_count < 2:
        discount = 0.0
        grand_total = total
    else:
        discount = total * Decimal(settings.DISCOUNT_PERCENTAGE / 100)
        grand_total = total - discount

    context = {
        'bag_items': bag_items,
        'total': total,
        'graphic_count': graphic_count,
        'discount': discount,
        'discount_percentage': settings.DISCOUNT_PERCENTAGE,
        'grand_total': grand_total,
    }

    return context
