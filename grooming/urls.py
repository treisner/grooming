from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from customers.views import CustomerCreate, CustomerUpdate, CustomerDelete, CustomerListView, CallListView
from customers.views import BreedDelete, PetListView, BreedListView, BreedUpdateView, BreedCreateView
from customers.views import ServiceDelete,  ServiceListView,ServiceUpdateView, ServiceCreateView
from customers.views import PetDelete,PetUpdate, AppointmentUpdate,AppointmentDelete, AppointmentListView

urlpatterns = patterns('',
    url(r'^$', "customers.views.home_view",name="home"),
    url(r'^customer/create/',CustomerCreate.as_view(), {'phone':'callername'},name="customer_create"),
    url(r'^customer/(?P<pk>[0-9]+)/$',CustomerUpdate.as_view(), name="customer_update"),
    url(r'^customer/delete/(?P<pk>[0-9]+)/$',CustomerDelete.as_view(), name="customer_delete"),
    url(r'^customers/$',CustomerListView.as_view(),name="customer_list"),
    url(r'^breed/delete/(?P<pk>[0-9]+)/$',BreedDelete.as_view(), name="breed_delete"),
    url(r'^breeds/$', BreedListView.as_view(),name="breed_list"),
    url(r'^breed/(?P<pk>[0-9]+)/$', BreedUpdateView.as_view(),name="breed_update"),
    url(r'^breed/create/$', BreedCreateView.as_view(),name="breed_create"),
    url(r'^service/delete/(?P<pk>[0-9]+)/$',ServiceDelete.as_view(), name="service_delete"),
    url(r'^services/$', ServiceListView.as_view(),name="service_list"),
    url(r'^service/(?P<pk>[0-9]+)/$', ServiceUpdateView.as_view(),name="service_update"),
    url(r'^service/create/$', ServiceCreateView.as_view(),name="service_create"),
    url(r'^pet/delete/(?P<pk>[0-9]+)/$',PetDelete.as_view(), name="pet_delete"),
    url(r'^pets/$', PetListView.as_view(),name="pet_list"),
    url(r'^pet/(?P<pk>[0-9]+)/$', PetUpdate.as_view(),name="pet_update"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^logout/$','customers.views.logout_view',name='logout'),
    url(r'^(accounts/)?login/(.*)$','customers.views.login_view',name='login'),
    url(r'^accounts/auth/$','customers.views.auth_view',name='auth'),
    url(r'^freetime/(.*)/(.*)/(next)$', 'customers.views.freetime',name='freetime'),
    url(r'^freetime/(.*)/(.*)/$', 'customers.views.freetime',name='freetime'),
    url(r'^freetime/(.*)/$', 'customers.views.freetime',name='freetime'),
    url(r'^freetime/(?P<pk>[0-9]+)/$', 'customers.views.freetime',name='freetime'),
    url(r'^oauth2callback', 'customers.views.auth_return'),
    url(r'^appointment/create/(.*)/(.*)/(.*)/$', "customers.views.make_appointment",name="appoinment_create"),
    url(r'^appointment/(?P<pk>[0-9]+)/$',AppointmentUpdate.as_view(),name="appointment_update"),
    url(r'^appointment/delete/(?P<pk>[0-9]+)/$',AppointmentDelete.as_view(),name="appointment_delete"),
    url(r'^appointments/(.*)$', AppointmentListView.as_view(),name="appointment_list"),
    url(r'^time/','customers.views.time_view',name='time'),
    url(r'^calls/',CallListView.as_view(),name="call_list"),


) + staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






