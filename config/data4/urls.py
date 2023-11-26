from django.urls import path
from .views import Seven

urlpatterns = [
    path('', Seven.as_view(), name='seven'),
]