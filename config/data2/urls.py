from django.urls import path
from .views import Five

urlpatterns = [
    path('', Five.as_view(), name='five'),
]