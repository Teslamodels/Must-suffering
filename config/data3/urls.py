from django.urls import path
from .views import Six

urlpatterns = [
    path('', Six.as_view(), name='six'),
]