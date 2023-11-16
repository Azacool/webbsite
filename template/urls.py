from django.urls import path
from .views import index, about,service,why,team

urlpatterns = [
    path('',index),
    path('about.html/',about),
    path('service.html/',service),
    path('why.html/',why),
    path('team.html/',team),
    
]