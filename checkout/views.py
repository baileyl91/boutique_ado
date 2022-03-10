from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': pk_test_51KbpWMHw3aNsVabkdiRSsaqybeyzh3ma7bspuZVw5dH0iH8ebKqtTAZsjodrINRpfUNJEFGfXnDvKzkukyH33qog00H8NotC1o,
        'client_secrect':  'test client secrect',
    }

    return render(request, template, context)