from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
#the r is to prevent line jumps or tabs programmers/1
router.register(r'programmers', views.ProgrammerViewSet)

urlpatterns = [
    path('', include(router.urls))
]