from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^(?P<search_id>[0-9]+)/page/(?P<page>[0-9]+)$', views.detail, name='detail'),
]