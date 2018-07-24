from django.conf.urls import url

urlpatterns = [
    url(r'^position/(?P<slug>[\w-]+)/$', 'apps.matches.views.position_match_view', name='position_match_view_url'),
    url(r'^employer/(?P<slug>[\w-]+)/$', 'apps.matches.views.employer_match_view', name='employer_match_view_url'),
    url(r'^location/(?P<slug>[\w-]+)/$', 'apps.matches.views.location_match_view', name='location_match_view_url'),
]
