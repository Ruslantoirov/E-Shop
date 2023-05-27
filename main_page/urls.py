from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page,name='main_page'),
    path('product/<int:pk>', views.get_full_product),
    path('category/<int:pk>', views.get_full_category),
    path('search',views.search_exact_product),
    path('add_to_cart/<int:pk>', views.add_products_to_user_card),
    path('user_cart', views.user_cart),
    path('delete_product/<int:pk>', views.delete_exact_user_cart),
    #path('order_product', views.order_user_product),

    path('login', views.CustomLoginView.as_view()),
    path('logout', views.LogoutView.as_view()),
]
