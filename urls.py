from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import  CeatePost,PostView,CeateVacancy,VacancyView,CeateFollow,FollowView

urlpatterns = [
    url(r'^Post/$', CeatePost.as_view(), name="createPost"), 
    url(r'^post/(?P<pk>[0-9]+)/$',PostView.as_view(), name="detailsPost"),
    url(r'^Vacancy/$', CeateVacancy.as_view(), name="createVacancy"), 
    url(r'^Vacancy/(?P<pk>[0-9]+)/$',VacancyView.as_view(), name="detailsVacancy"),
    url(r'^Follow/$', CeateFollow.as_view(), name="CreatFollow"), 
    url(r'^Follow/(?P<pk>[0-9]+)/$',FollowView.as_view(), name="detailsFollow"),
]
urlpatterns = format_suffix_patterns(urlpatterns)