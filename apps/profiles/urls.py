from django.conf.urls import url

urlpatterns = [
    url(r'^profile/edit/$', 'apps.profiles.views.profile_edit', name='profile_edit'),
    url(r'^profile/(?P<username>[\w.@+-]+)/$', 'apps.profiles.views.profile_view', name='profile'),
    url(r'^profile/jobs/add/$', 'apps.profiles.views.job_add', name='job_add'),
    url(r'^profile/jobs/edit/$', 'apps.profiles.views.jobs_edit', name='jobs_edit'),
    url(r'^profile/$', 'apps.profiles.views.profile_user', name='profile_user'),
]
