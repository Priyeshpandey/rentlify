from django.urls import path
from buyer.views import home

urlpatterns = [
    path('home/', home, name='buyer'),
]
