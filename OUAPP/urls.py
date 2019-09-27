from django.urls import path, include
from django.conf.urls import url
from django.urls import path
from django.views.generic import RedirectView
from . import views
#from . import config
urlpatterns =[
    # path('<str:slug>', views.index, name='index'),    
    url(r'^$', views.index, name='index'),
    url(r'^$', views.feed, name='feed'),
    
]
