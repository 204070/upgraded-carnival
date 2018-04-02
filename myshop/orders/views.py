from django.shortcuts import redirect, render, reverse

from cart.cart import Cart

from .forms import OrderCreateForm
from .models import OrderItem
from .tasks import order_created

# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                new_order = OrderItem(order=order, product = item['product'],
                                        price=item['price'],
                                        quantity=item['quantity'])
                new_order.save()
            cart.clear()
            # launch asynchronous task
            order_created.delay(order.id) # set the order in the session
            request.session['order_id'] = order.id # redirect to the payment
            return redirect(reverse('payments:process'))
    else:
        form = OrderCreateForm()
    return render(request, 'orders/order/create.html',
                    {'cart': cart, 'form': form})
