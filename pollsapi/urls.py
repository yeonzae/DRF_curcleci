from django.urls import include, re_path, path
from django.contrib import admin

urlpatterns = [
    re_path(r'^', include('polls.urls')),
    path("admin/", admin.site.urls),

]