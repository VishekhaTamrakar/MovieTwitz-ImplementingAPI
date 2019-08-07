from django.shortcuts import render, redirect
from .models import OrderItem
from mtapp.models import Product
from .forms import OrderCreateForm
from cart.cart import Cart
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .models import Order
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required()
def order_create(request, pk):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            updateOrder = Order.objects.latest('id')
            updateOrder.cust_num = User.objects.get(pk=pk)
            updateOrder.save()
            for item in cart:
                OrderItem.objects.create(order=order,product=item['product'],price=item['price'],
                                         quantity=item['quantity'])

            # clear the cart
            cart.clear()
            # launch asynchronous task
            # order_created.delay(order.id)
            # set the order in the session
            request.session['order_id'] = order.id
            # redirect for payment
            return redirect(reverse('payment:process'))
    else:
        form = OrderCreateForm()
    return render(request,'orders/order/create.html',{'cart': cart, 'form': form})

def order_list(request):
    orders = Order.objects.filter()
    order_count = orders.count()

    return render(request,'app/admin_order_list.html', {'orders': orders, 'order_count': order_count})

def order_detail(request, id) :
    orderinline = OrderItem.objects.filter(order_id=id)
    order_item = get_object_or_404(Order, pk=id)
    print(order_item.first_name, order_item.last_name, sep=', ')
    total_amount = 0
    for order in orderinline.iterator():
        total_amount = total_amount + (order.price * order.quantity)

    products = Product.objects.filter()
    return render(request, 'app/order_details.html', {'orderdetails': orderinline,
                                                      'product': products,
                                                      'order_item': order_item,
                                                      'total_amount': total_amount})

def customer_order(request,id) :
    try:
        orders = Order.objects.filter(cust_num=id)
        order_count = orders.count()
        return render(request,'app/my_order.html',{'orders':orders,'order_count': order_count})
    except Order.DoesNotExist:
        return render(request, 'app/my_order.html', {'orders': None, 'order_count': 0})