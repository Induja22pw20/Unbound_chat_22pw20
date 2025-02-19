
from django.urls import path
from .views import models_list, index

urlpatterns = [
    path('', index, name='index'),
    path('models/', models_list, name='models_list'),
]
