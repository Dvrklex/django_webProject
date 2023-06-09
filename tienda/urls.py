from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.tienda, name='Tienda'),
    path('product/<int:product_id>/', views.view_product, name='view_product'),
    path('carrito/', views.view_carrito, name='Carrito'),
    path('categoria/<int:categoria_id>/', views.categoria_producto, name='Categoria'),
    path('search/', views.search_bar, name='Search'),


    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 