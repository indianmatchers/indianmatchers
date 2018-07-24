from django.conf.urls import url

# app urls
urlpatterns = [
    url(r'^like/(?P<id>\d+)/$', 'apps.likes.views.like_user', name='like_user')
]
