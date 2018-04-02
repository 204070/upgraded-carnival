import hashlib
import hmac
import httplib
import json
from decimal import Decimal

from django.shortcuts import get_object_or_404, render
from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from orders.models import Order

# Create your views here.

def payment_process(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)

    amount = order.get_total_cost()
    email = order.email
    return render(request, 'payments/process.html', {'amount': amount,
                                                    'email': email})


def payment_done(request):
    return render(request, 'payments/done.html')

def payment_canceled(request):
    return render(request, 'payments/canceled.html')

def handle_webhook(event, payload):
    order_id = 
@csrf_exempt
def handle_paystack_hook(request):
    # Check the X-Paystack-Signature header to make sure this is a valid request.
    paystack_signature = request.META['HTTP_X_PAYSTACK_SIGNATURE']
    signature = hmac.new(settings.PAYSTACK_SECRET_KEY, request.body, hashlib.sha512)
    expected_signature = 'sha512=' + signature.hexdigest()
    if not hmac.compare_digest(paystack_signature, expected_signature):
        return HttpResponseForbidden('Invalid signature header')

    payload = json.loads(request.body)
    event = payload['event']

    # This is where you'll do something with the webhook
    handle_webhook(event, payload)

    return HttpResponse('Webhook received', status=httplib.ACCEPTED)
