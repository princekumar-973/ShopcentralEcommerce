from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Order, OrderItem, Wishlist
from .cart import Cart


def product_list(request):
    products      = Product.objects.filter(available=True)
    categories    = Category.objects.all()
    
    # Search logic
    query = request.GET.get('q')
    if query:
        products = products.filter(
            Q(name__icontains=query) | 
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        )

    # Category Filter (Multiple)
    category_slugs = request.GET.getlist('category')
    if category_slugs and 'all' not in category_slugs:
        products = products.filter(category__slug__in=category_slugs)

    # Price Filter
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)

    # Sorting
    sort = request.GET.get('sort')
    if sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    elif sort == 'newest':
        products = products.order_by('-created_at')

    return render(request, 'store/product_list.html', {
        'products':            products,
        'categories':          categories,
        'query':               query,
        'selected_categories': category_slugs,
        'min_price':           min_price,
        'max_price':           max_price,
        'sort':                sort,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'store/product_detail.html', {'product': product})


def home(request):
    featured_products = Product.objects.filter(available=True)[:8]
    return render(request, 'store/home.html', {
        'featured_products': featured_products,
    })


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'store/cart.html', {'cart': cart})


@login_required
def cart_add(request, product_id):
    cart     = Cart(request)
    product  = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    size     = request.POST.get('size', '').strip()

    # If product has sizes but none selected → show error
    if product.has_sizes and not size:
        return render(request, 'store/product_detail.html', {
            'product':    product,
            'size_error': 'Please select a size before adding to cart.'
        })

    cart.add(product, quantity, size)
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'status': 'success',
            'cart_count': len(cart),
            'cart_total': str(cart.get_total())
        })

    return redirect('store:cart_detail')


@login_required
def cart_remove(request, product_id):
    if request.method != 'POST':
        return redirect('store:cart_detail')
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    size = (request.POST.get('size') or '').strip()
    cart.remove(product, size)
    return redirect('store:cart_detail')


@login_required
def place_order(request):
    cart = Cart(request)

    if not cart:
        return redirect('store:cart_detail')

    if request.method == 'POST':
        payment_method = request.POST.get('payment', 'cod')
        address        = request.POST.get('address', '').strip()
        city           = request.POST.get('city', '').strip()
        state          = request.POST.get('state', '').strip()
        pincode        = request.POST.get('pincode', '').strip()

        if not address or not city or not state or not pincode:
            return render(request, 'store/cart.html', {
                'cart':  cart,
                'error': 'Please fill in all delivery address fields before placing order.'
            })

        order = Order.objects.create(
            user           = request.user,
            payment_method = payment_method,
            total_amount   = cart.get_total(),
            address        = address,
            city           = city,
            state          = state,
            pincode        = pincode,
        )

        for item in cart:
            OrderItem.objects.create(
                order    = order,
                product  = item['product'],
                size     = item.get('size', ''),
                quantity = item['quantity'],
                price    = item['price'],
            )

        # Save address to profile for next time
        request.user.profile.address = address
        request.user.profile.city    = city
        request.user.profile.state   = state
        request.user.profile.pincode = pincode
        request.user.profile.save()

        cart.clear()
        return redirect('store:order_success', order_id=order.id)

    return redirect('store:cart_detail')


@login_required
def order_success(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'store/order_success.html', {'order': order})


def contact(request):
    if request.method == 'POST':
        # In a real app, you would send an email here
        messages.success(request, 'Your message has been sent successfully! We will get back to you soon.')
        return redirect('store:contact')
    return render(request, 'store/contact.html')


@login_required
def wishlist_toggle(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    wishlist_item = Wishlist.objects.filter(user=request.user, product=product)
    
    if wishlist_item.exists():
        wishlist_item.delete()
        added = False
    else:
        Wishlist.objects.create(user=request.user, product=product)
        added = True
        
    return JsonResponse({'added': added})


@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'store/my_orders.html', {'orders': orders})