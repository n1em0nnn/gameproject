from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, CartItem, Purchase, Notification
from teachers.models import ChildProfile, Teacher
from .forms import AddToCartForm

@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    child = request.user.childprofile

    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            cart_item, created = CartItem.objects.get_or_create(
                child_profile=child,
                product=product,
                defaults={'quantity': quantity}
            )
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
            return redirect('cart_view')
    else:
        form = AddToCartForm()
    return render(request, 'shop/add_to_cart.html', {'form': form, 'product': product})

@login_required
def cart_view(request):
    child = request.user.childprofile
    cart_items = child.cart_items.all()
    total_cost = sum(item.total_price() for item in cart_items)
    return render(request, 'shop/cart_view.html', {'cart_items': cart_items, 'total_cost': total_cost})

@login_required
def checkout(request):
    child = request.user.childprofile
    cart_items = child.cart_items.all()
    total_cost = sum(item.total_price() for item in cart_items)

    if child.points < total_cost:
        return render(request, 'shop/checkout_error.html', {'message': 'Not enough points!'})  # Если баллов недостаточно

    # Создаем записи о покупках
    for cart_item in cart_items:
        Purchase.objects.create(
            child_profile=child,
            product=cart_item.product,
            quantity=cart_item.quantity,
            total_price=cart_item.total_price()
        )

        # Уменьшаем количество товара на складе
        cart_item.product.stock -= cart_item.quantity
        cart_item.product.save()

    # Вычитаем баллы из счета ученика
    child.points -= total_cost
    child.save()

    # Отправляем уведомление преподавателю
    teacher = child.teacher
    Notification.objects.create(
        teacher=teacher,
        message=f"{child.full_name} purchased items worth {total_cost} points."
    )

    # Очищаем корзину
    cart_items.delete()

    return redirect('purchase_success')

@login_required
def purchase_success(request):
    return render(request, 'shop/purchase_success.html')