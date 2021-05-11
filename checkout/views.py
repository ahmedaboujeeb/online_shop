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
        'stripe_public_key': 'pk_test_51IpsIQIHH9h4Wbq5E3eRjo6XfyXRqLLOj0iYIwqd4K3bUgfpTLPIgEFkhNQCxP5wxTDh8yhh9E3fmyA3XRaQ4Sze00WwH9Doxa',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)