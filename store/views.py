from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Product, Cart, Order
from .forms import RegisterForm, ProductForm


# Home Page

def home(request):

    return render(
        request,
        'home.html'
    )


# Register

def register(request):

    form = RegisterForm(
        request.POST or None
    )

    if form.is_valid():

        form.save()

        return redirect('login')

    return render(
        request,
        'register.html',
        {'form': form}
    )


# Login

def login_view(request):

    if request.method == "POST":

        username = request.POST.get('username')

        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(
                request,
                user
            )

            return redirect(
                'products'
            )

    return render(
        request,
        'login.html'
    )


# Logout

def logout_view(request):

    logout(request)

    return redirect(
        'login'
    )


# Products List

def product_list(request):

    products = Product.objects.all()

    return render(

        request,

        'product_list.html',

        {'products': products}

    )


# Single Product

def product_detail(request, id):

    product = get_object_or_404(
        Product,
        id=id
    )

    return render(

        request,

        'product_detail.html',

        {'product': product}

    )


# Add Product

@login_required
def add_product(request):

    form = ProductForm(

        request.POST or None,

        request.FILES or None

    )

    if form.is_valid():

        form.save()

        return redirect(
            'products'
        )

    return render(

        request,

        'add_product.html',

        {'form': form}

    )


# Update Product

@login_required
def update_product(request, id):

    product = Product.objects.get(
        id=id
    )

    form = ProductForm(

        request.POST or None,

        request.FILES or None,

        instance=product

    )

    if form.is_valid():

        form.save()

        return redirect(
            'products'
        )

    return render(

        request,

        'update_product.html',

        {

            'form': form,

            'product': product

        }

    )


# Delete Product

@login_required
def delete_product(request, id):

    product = Product.objects.get(
        id=id
    )

    if request.method == "POST":

        product.delete()

        return redirect(
            'products'
        )

    return render(

        request,

        'delete_product.html',

        {'product': product}

    )


# Add Cart

@login_required
def add_cart(request, id):

    product = Product.objects.get(
        id=id
    )

    Cart.objects.create(

        user=request.user,

        product=product,

        quantity=1

    )

    return redirect(
        'cart'
    )


# Cart Page

@login_required
def cart(request):

    items = Cart.objects.filter(
        user=request.user
    )

    return render(

        request,

        'cart.html',

        {'items': items}

    )


# Checkout

@login_required
def checkout(request):

    if request.method == "POST":

        items = Cart.objects.filter(
            user=request.user
        )

        for item in items:

            Order.objects.create(

                user=request.user,

                product=item.product,

                quantity=item.quantity

            )

        items.delete()

        return redirect(
            'orders'
        )

    return render(
        request,
        'checkout.html'
    )


# Orders

@login_required
def orders(request):

    all_orders = Order.objects.filter(
        user=request.user
    )

    return render(

        request,

        'orders.html',

        {'orders': all_orders}

    )


# Order Details

@login_required
def order_detail(request, id):

    order = Order.objects.get(
        id=id
    )

    return render(

        request,

        'order_detail.html',

        {'order': order}

    )


# Profile

@login_required
def profile(request):

    return render(
        request,
        'profile.html'
    )