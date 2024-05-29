from django.urls import path 
from newyear.views import newyear



urlpatterns = [
    path('', newyear, name='newyear')
]