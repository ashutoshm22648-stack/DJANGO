from django.urls import path

from DJANGOAPP.views import view1

urlpatterns = [
    path('view1/', view1,name='view1'),
]
