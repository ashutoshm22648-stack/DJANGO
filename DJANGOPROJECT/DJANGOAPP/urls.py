from django.urls import path

from DJANGOAPP.views import view1
from DJANGOAPP.views import *



urlpatterns = [
    path('view1/', view1,name='view1'), 
    path('sum/', sum,name='sum'),
    path('now/', date, name='now'),
    path('home/', home, name='home'),
    path('about/', aboutus, name='about'),


]
