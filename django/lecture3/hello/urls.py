from django.urls import path
from hello.views import index, spencer, greet

urlpatterns = [
    path('', index, name='index'),
    path('spl/', spencer, name='spencer'),
    path('<str:name>/', greet, name='greet'),
]
