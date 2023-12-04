# Create your views here.
import uuid
from item.models import Item
from django.urls import reverse
from django.conf import settings
from paypal.standard.forms import PayPalPaymentsForm
from django.shortcuts import render, get_object_or_404


def checkout(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    host = request.get_host()
    # Add your checkout logic here

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': item.price,
        'item_name': item.name,
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('checkout:payment-success', kwargs = {'item_pk': item.id})}",
        'cancel_url': f"http://{host}{reverse('checkout:payment-failed', kwargs = {'item_pk': item.id})}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    context = {
        'item': item,   
        'paypal': paypal_payment

    }

    return render(request, 'checkout.html', context)


# Create your views here.

# def CheckOut(request, item_pk):

#     item = get_object_or_404(Item, pk=item_pk)

#     context = {
#         'item': item,
        
#     }

#     return render(request, 'checkout.html', context)


def PaymentSuccessful(request, item_pk):

    item = get_object_or_404(Item, pk=item_pk)

    return render(request, 'payment-success.html', {'item': item})

def paymentFailed(request, item_pk):

    item = get_object_or_404(Item, pk=item_pk)

    return render(request, 'payment-failed.html', {'item': item})