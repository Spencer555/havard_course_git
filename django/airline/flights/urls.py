from django.urls import path
from . import views

app_name = 'flights'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.flight, name='detail'),
    path('<int:id>/book/', views.book, name='book'),
]
