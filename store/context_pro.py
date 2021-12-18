from .models import Category, Product
from cart.models import Cart

def view_all(request):
    try:
        cart = Cart.objects.get(id=request.session.get('user_cart_id'))
    except:
        cart = {'status': 'Cart is not defined!'}
    print(cart)

    # qs = Product.objects.all()
    # my_random_object = random.sample(qs,1)
    context = {
        "categories":Category.objects.all(),
        "cart":cart
    }
    return context