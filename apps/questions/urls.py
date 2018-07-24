from django.conf.urls import url

# app urls
urlpatterns = [
    url(r'^question/(?P<id>\d+)/$', 'apps.questions.views.single', name='question_single'),
    url(r'^question/$', 'apps.questions.views.home', name='question_home')
]
