from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.market.catalog, name='catalog'), 
    path('login/', views.auth.login, name="login"),
    path('signup/', views.auth.signup, name="signup"),
    path('product/<int:pk>/info', views.market.product_info, name='product_info'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)