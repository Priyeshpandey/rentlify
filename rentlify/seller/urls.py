from django.urls import path
from seller.views import home

urlpatterns = [
    path('home/', home, name='seller'),
]
