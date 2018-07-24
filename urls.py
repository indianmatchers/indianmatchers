from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', admin.site.urls),
]

# app urls
urlpatterns += [
    url(r'^', include('apps.dashboard.urls')),
    url(r'^', include('apps.questions.urls')),
    url(r'^', include('apps.profiles.urls')),
    url(r'^', include('apps.newsletter.urls')),
    url(r'^', include('apps.likes.urls')),
    url(r'^matches/', include('apps.matches.urls')),

    url(r'^accounts/', include('registration.backends.default.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Change to whatever you like
admin.site.site_title = 'strangematcher Administration'
admin.site.index_title = 'strangematcher Administration'
admin.site.site_header = 'strangematcher Administration'
