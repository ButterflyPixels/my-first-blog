from django.conf.url import url
from . import views

urlpatters = [
    url(r'^$', views.post_list, name='post_list'),
]
