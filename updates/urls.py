from django.conf.urls import url

from django.urls import path
from updates import views

urlpatterns =[
    path('', views.update_model_list_view)
]