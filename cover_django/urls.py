from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cover_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
)
