from django.urls import path 
from tasks.views import index, add


app_name = 'tasks'


urlpatterns = [
    path('', index, name='index'),
    path('add/', add, name='add')
]