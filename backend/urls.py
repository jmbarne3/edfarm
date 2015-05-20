from django.conf.urls import include, url, patterns
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = patterns('',
	url(r'^$', login_required(ManagerHomeView.as_view()), name='manager-dashboard'),
	url(r'^home-page/$', login_required(HomePageUpdate.as_view()), name='manager-home-page'),
	url(r'^home-page/centerpieces/create/$', login_required(CenterpieceCreateView.as_view()), name="manager-centerpiece-create"),
	url(r'^home-page/centerpieces/update/(?P<pk>\d+)/$', login_required(CenterpieceUpdateView.as_view()), name="manager-centerpiece-update"),
	url(r'^home-page/announcements/create/$', login_required(AnnouncementCreateView.as_view()), name="manager-announcement-create"),
	url(r'^home-page/announcements/update/(?P<pk>\d+)/$',login_required(AnnouncementUpdateView.as_view()), name="manager-announcement-update"),

	url(r'^products/$', login_required(ProductListView.as_view()), name="manager-product-list"),
	url(r'^products/create/$', login_required(ProductCreateView.as_view()), name="manager-product-create"),
	url(r'^products/(?P<pk>\d+)/update/$', login_required(ProductUpdateView.as_view()), name="manager-product-update"),
)