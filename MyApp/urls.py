from django.urls import path
from .views import *
urlpatterns=[
    path('',Login,name="Login/"),
    path('Register/',Register,name="Register/"),
    path('Dashboard/',Dashboard,name="Dashboard/"),
    path('Logout/',Logout,name="Logout/"),
    path('AddCustomer/',AddCustomer,name="AddCustomer/"),
    path('ViewCustomer/',ViewCustomer,name="ViewCustomer/"),
    path('DeleteCustomer/<int:id>',DeleteCustomer,name="DeleteCustomer/"),
    path('UpdateCustomer/<int:id>',UpdateCustomer,name="UpdateCustomer/"),
    path('Orders/',Orders,name="Orders/"),
]