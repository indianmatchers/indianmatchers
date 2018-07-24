from django.conf.urls import url

urlpatterns = [
    url(r'^contact/$', 'apps.newsletter.views.contact', name='contact')
]
