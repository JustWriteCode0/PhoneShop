from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Users.urls')),
    path('cart/', include('Cart.urls')),
    path('', include('Products.urls')),
    path('orders/', include('Orders.urls')),
]
