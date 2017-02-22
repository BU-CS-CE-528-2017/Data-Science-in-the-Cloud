from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$|index$', views.index, name='index'),
    url(r'^success|SUCCESS$', views.success, name="success"),
    url(r'^generate|Generate$', views.generate, name="generate"),
    url(r'^process|PROCESS$', views.process, name="generate"),

]
