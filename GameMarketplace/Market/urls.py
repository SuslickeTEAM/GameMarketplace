from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.market.catalog, name='catalog'), 
    path('login/', views.auth.login, name="login"),
    path('signup/', views.auth.signup, name="signup"),
    path('product/<int:pk>/info', views.market.product_info, name='product_info'),
    path('basket/', views.basket.view_basket, name='view_basket'), 
    path('basket/buy', views.buy.BuyProduct, name='buy'),
    path('basket/buy/<int:pk>/confirm-buy/', views.buy.BuyConfirm, name='confirm-buy'),
    path('basket/<int:pk>/add', views.basket.add_basket, name='add_basket'), 
    path('basket/<int:basket>/product/<int:product>/remove',views.basket.subtraction_basket, name='subtraction_basket'),
    path('basket/<int:basket>/product/<int:product>/add',views.basket.addition_basket, name='addition_basket'),
    path('profile/', views.profile.profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)