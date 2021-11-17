from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    # prevent users from adding /checkout to access checkout
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Jj2kiHUE1qNx3daPSjMWFy8nmnW5FCB7ywFoBsnUi9dLRywzydfUK9JLOLEjJfPIT6CzYWOyzPuzSQEnglnEeKW002FkVkSCQ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
