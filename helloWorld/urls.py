from django.conf.urls import patterns, url
from helloWorld.views import HomePageView

urlpatterns = patterns(
    '',

    url(r'^$', HomePageView.as_view(), name='home'),
)
