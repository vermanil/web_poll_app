from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^(?P<ques_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<ques_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<ques_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^$', views.indexing, name='indexing')
]