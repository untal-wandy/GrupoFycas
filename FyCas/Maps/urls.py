from django.contrib import admin
from django.urls import path, include
from . import views

app_name = "maps"
urlpatterns = [
      path('maps/customer', views.Maps.as_view(), name='maps-customer'),
      path('data-credito/', views.DataCredit.as_view(), name='data-credi')
      
]