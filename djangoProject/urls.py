
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('accounts.urls')),

]
