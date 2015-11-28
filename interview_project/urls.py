from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_element/(?P<element_id>[0-9]+)/$', views.get_element, name='get_element'),
    url(r'^generate$', views.generate, name='generate'),
]