from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()



router.register(r'status', StatusViewSet, basename='status')

urlpatterns = [ 
    path('',include(router.urls)),
]