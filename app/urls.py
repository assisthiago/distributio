from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from app.core.views import UserViewSet

# Overriding AdminSite attributes.
admin.site.site_header = admin.site.site_title = "DISTRIBUTIO"

# API URLs.
router = routers.SimpleRouter()
router.register("users", UserViewSet, basename="user")

urlpatterns = [
    path("api/", include(router.urls)),  # API URLs
]

# Include debug toolbar URLs.
if settings.DEBUG:
    urlpatterns += [
        path("admin/", admin.site.urls),  # Admin URLs
        path("api-auth/", include("rest_framework.urls")),  # REST framework auth URLs
    ]
    urlpatterns += debug_toolbar_urls()  # Debug toolbar URLs

# Include static URLs.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
