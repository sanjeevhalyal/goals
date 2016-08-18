from django.conf.urls import url
from . import views

app_name='goal'
urlpatterns = [
    url(r'^$', views.task, name='task'),
    url(r'^daliy/$', views.daliy, name='daliy'),
    url(r'^newdaliy/$', views.newdaliy, name='newdaliy'),
    url(r'^newtask/$', views.newtask, name='newtask'),
    url(r'^deltoday/$', views.deltoday, name='deltoday'),
    url(r'^minitask/$', views.minitask, name='minitask'),
]