from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Category, Product, Cart
from .handlers import bot

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main_page')


# Create your views here.
def main_page(request):
    #Собираем все названия продуктов
    product_info = Product.objects.all()

    #Собираем все названия категорий
    category_info = Category.objects.all()

    context = {'products': product_info, 'categories': category_info}
    return render(request, 'index.html', context)

def get_full_product(request, pk):
    product = Product.objects.get(id=pk)

    context = {'product': product}
    return render(request, 'exact_product.html', context)

def get_full_category(request, pk):
    category = Category.objects.get(id=pk)
    products = Product.objects.filter(category_name=category)

    context = {'products': products}

    return render(request, 'exact_category.html', context)

def search_exact_product(request):
    if request.method == 'POST':
        get_product = request.POST.get('search_product')

        try:
            exact_product = Product.objects.get(product_name__icontains=get_product)

            return redirect(f'product/{exact_product.id}')

        except:
            return redirect('/')

def add_products_to_user_card(request, pk):
    if request.method == "POST":
        checker = Product.objects.get(id=pk)

        if checker.product_amount >= int(request.POST.get('pr_count')):
            Cart.objects.create(user_id=request.user.id,
                                user_product=checker,
                                user_product_quantity=int(request.POST.get('pr_count'))).save()

            return redirect('/')

        else:
            return redirect(f'/product/{checker.id}')

def user_cart(request):
    cart = Cart.objects.filter(user_id=request.user.id)

    if request.method == 'POST':
        main_text = 'Новый заказ\n\n'

        for i in cart:
            main_text += f'Товар: {i.user_product}\n'\
                         f'Количество: {i.user_product_quantity}\n'
        bot.send_message(1070146947, main_text)
        cart.delete()
        return redirect('/')

    return render(request, 'user_cart.html', {'cart': cart})

def delete_exact_user_cart(request, pk):
    product_to_delete = Product.objects.get(id=pk)

    user_products = Cart.objects.filter(user_id=request.uesr.id,
                                        user_product=product_to_delete).delete()

    return redirect('/user_cart')

