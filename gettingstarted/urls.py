from django.urls import path, include
from django.urls import path
from django.contrib import admin
from django.conf.urls import include, url
admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("get_event_names/", hello.views.get_event_names, name="get_event_names"),
    path("get_sample_data/<str:event_name>/<int:count>/", hello.views.get_sample_data, name="get_sample_data"),
    path("get_tweet_with_id/<str:event_name>/<str:tweet_id>/", hello.views.get_tweet_with_id, name="get_tweet_with_id"),
    # path("data/", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
]
