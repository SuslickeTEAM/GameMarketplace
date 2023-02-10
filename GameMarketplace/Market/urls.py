from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.market.index, name='index'),
    path('catalog/', views.market.catalog, name='catalog'),
    path('catalog/filter/', views.market.catalog_filter, name='filter'),
    path('login/', views.auth.login, name="login"),
    path('signup/', views.auth.signup, name="signup"),
    path('logout/', views.auth.logout_view, name='logout'),
    path('basket/', views.basket.view_basket, name='view_basket'), 
    path('basket/<int:pk>/add', views.basket.add_basket, name='add_basket'), 
    path('basket/<int:basket>/product/<int:product>/remove',views.basket.subtraction_basket, name='subtraction_basket'),
    path('basket/<int:basket>/product/<int:product>/add',views.basket.addition_basket, name='addition_basket'),
    path('profile/', views.profile.profile, name='profile'),
    path('profile/history/<int:history_id>', views.profile.get_data, name='profile_history'),
    
    path('basket/buy/<uuid:order_num>', views.buy.buy_product, name='buy'),
    # path('payment/validation/', views.buy.payment_validation, name='payment_validation'),
    path('basket/buy/<uuid:pk>/confirm-buy/', views.buy.buy_confirm, name='confirm-buy'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)