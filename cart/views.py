from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Cart
from .forms import OrderForm

# Create your views here.

def cart_init(request):
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        cart = Cart.objects.create()
        request.session['user_cart_id'] = cart.id
    return cart


def cartView(request):
    cart = cart_init(request)
    return render(request,"cart/cart.html", {"cart":cart})


import json
def addToCart(request):
    print(request)
    d = request.GET.get('data')
    data  = json.loads(d)
    print(data)
    product_id = data['product_id']
    quantity = data['count']
    cart = cart_init(request)
    cart.add(product_id,quantity)
    status = {

    }
    if cart:
        status['success'] = 200
    else:
        status['error'] = 400
    return JsonResponse(status)

def deleteCartItem(request,product_id,qty):
    cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    cart.deleteItem(product_id,qty)
    return redirect('cart:cart')

def removeCartItems(request):
    cart = cart_init(request)
    cart.removeAllItems()
    return redirect('cart:cart')

def checkout(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            cart = cart_init(request)
            f.products = cart
            f.user = request.user
            f.save()
    else:
        form = OrderForm()
    return render(request, "cart/checkout.html", {"form":form})