from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('', include('search.urls')),
    path('admin/', admin.site.urls),
]
