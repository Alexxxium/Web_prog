from django.contrib.auth import views
from django.urls import path
from .views import *


urlpatterns = [ 
    path('', product, name='product_url'),
]
