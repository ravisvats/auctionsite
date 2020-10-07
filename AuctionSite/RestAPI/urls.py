from django.urls import path,include
from . import viewset
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    #API ENDPOINTS
    path('register/', csrf_exempt(viewset.Register.as_view()), name='register'),
]