from django.urls import path
from .views import (
    product_view_detail,
    product_create_view,
    product_delete_view,
    product_list_view,
    dynamic_lookup_view)

app_name = 'products'
urlpatterns= [
     path('<int:my_id>/delete/', product_delete_view, name='product-delete'),
     path('',product_list_view , name ='product-list'), 
     path('<int:id>/',product_view_detail, name='product-detail'),
     path('create/', product_create_view, name = 'product-list'),
     path('<int:my_id>/', dynamic_lookup_view, name='product'),
]