from django.conf.urls import include, url, patterns
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = patterns('',
	url(r'^$', login_required(ManagerHomeView.as_view()), name='manager-dashboard'),
	url(r'^home-page/$', login_required(HomePageUpdate.as_view()), name='manager-home-page-update'),
)