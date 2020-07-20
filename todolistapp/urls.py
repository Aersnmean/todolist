from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('items/', Items.as_view()),
    path('oneitem/<str:id>/', OneItem.as_view()),
    path('clear/', Clear.as_view())
]
