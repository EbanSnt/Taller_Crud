from main.views import *
from django.urls import path


urlpatterns = [
    path('', index, name="home"),
    path('new_customer', create_customer, name="new_customer"),
    path('new_ticket', create_ticket, name="new_ticket"),
    path('new_warranty_product', create_warranty_product, name="new_warranty_product"),
    path('new_delivered_product', create_delivered_product, name="new_delivered_product"),
    #####
    path('all_customers', show_all_customers, name="all_customers"),
    path('all_tickets', show_all_tickets, name="all_tickets"),
    path('all_warranty_products', show_all_warranty_products, name="all_warranty_products"),
    path('all_delivered_products', show_all_delivered_products, name="all_delivered_products"),
    #####
    path('update_customer/<int:customer_id>', update_customer, name="update_customer"),
]