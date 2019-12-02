from django.conf.urls import url
# from django.conf import settings
# from django.conf.urls.static import static

from . import views

app_name = 'neighborhood'

urlpatterns = [
    url(r"^$", views.ListGroups.as_view(), name="all"),
    url(r"^new/$", views.CreateGroup.as_view(), name="create"),
    url(r"^posts/in/(?P<slug>[-\w]+)/$",views.SingleGroup.as_view(),name="single"),
    url(r"^join/(?P<slug>[-\w]+)/$",views.JoinGroup.as_view(),name="join"),
    url(r"^leave/(?P<slug>[-\w]+)/$",views.LeaveGroup.as_view(),name="leave"),
    url(r"^search-results/$", views.search_results, name="search")
]

# if settings.DEBUG:
#     urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)