from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from products.models import Product
from .models import Cart, CartItem


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.user.cart
    cart.add_product(product)
    messages.success(request, f'{product.name} added to cart')
    return redirect('view_cart')  # Redirecting to the cart page


def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.user.cart
    cart.remove_product(product)
    messages.success(request, f'{product.name} removed from cart')
    return redirect('view_cart')  # Redirecting to the cart page


def clear_cart(request):
    cart = request.user.cart
    cart.clear_cart()
    messages.success(request, 'Cart cleared')
    return redirect('view_cart')  # Redirecting to the cart page


def view_cart(request):
    cart = request.user.cart
    items = cart.items.all()
    total_price = cart.get_total_price()
    return render(request, 'cart.html', {
        'cart': cart,
        'items': items,
        'total_price': total_price
    })


def update_cart_item(request, item_id):
    if request.method == 'POST':
        try:
            item = CartItem.objects.get(id=item_id)
            new_quantity = int(request.POST.get('quantity'))
            if new_quantity > 0:
                item.quantity = new_quantity
                item.save()
                # Recalculate the total price of the cart
                cart = item.cart
                cart.update_total_price()  # Assuming there's a method to update the total price
                cart.save()
                messages.success(request, 'Item quantity updated')
                return redirect('view_cart')  # Redirecting to the cart page
            else:
                messages.error(request, 'Quantity must be greater than zero')
                return redirect('view_cart')
        except CartItem.DoesNotExist:
            messages.error(request, 'Item not found in cart')
            return redirect('view_cart')
