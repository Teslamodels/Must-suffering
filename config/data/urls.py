from django.urls import path
from .views import One, Two, Three, Four

urlpatterns = [
    path('', One.as_view(), name='one'),
    path('apple/', Two.as_view(), name='two'),
    path('microsoft/', Three.as_view(), name='three'),
    path('tesla/', Four.as_view(), name='four'),
]