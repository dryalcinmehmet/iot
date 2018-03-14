
from django.conf.urls import url

from stark import views

urlpatterns = [


    url(r'^login/$', views.LoginFormControl.as_view(), name='login'),
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^veriler/$',views.VerilerPageView.as_view() , name='veriler'),
    url(r'^data/$', views.DataPageView.as_view(), name='data'),
    url(r'^test/$',views.TestPageView.as_view() , name='test'),


]