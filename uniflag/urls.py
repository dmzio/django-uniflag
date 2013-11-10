from django.conf.urls import patterns, url
from uniflag.views import FlagCreate, FlagUpdate

urlpatterns = patterns('',
                       url(r'add/$', FlagCreate.as_view(), name='flag_add'),
                       url(r'(?P<pk>\d+)/$', FlagUpdate.as_view(), name='flag_update'),
                       )
