from django.conf.urls import include, url, patterns
from .views import *

urlpatterns = patterns('',
	url(r'^$', HomeView.as_view(), name="home"),
	url(r'^accounts/login/$', LoginView.as_view(), name="login"),
	url(r'^typography/$', TypographyView.as_view(), name="typography"),
)