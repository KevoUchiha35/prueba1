from django.urls import path
from . import views
urlpatterns = [
    path('', views.kevo, name='kevo'),
    

]