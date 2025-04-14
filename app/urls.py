from debug_toolbar.toolbar import debug_toolbar_urls
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from app.category.views import AdditionalCategoryViewSet, ProductCategoryViewSet
from app.client.views import AddressViewSet, ClientViewSet, UserViewSet
from app.order.views import OrderViewSet
from app.product.views import AdditionalViewSet, ProductViewSet
from app.swagger import schema_view

# Overriding AdminSite attributes.
admin.site.site_header = admin.site.site_title = "DISTRIBUTIO"

# API URLs.
router = routers.SimpleRouter()

# Category
router.register(
    "additional-categories", AdditionalCategoryViewSet, basename="additional_category"
)
router.register(
    "product-categories", ProductCategoryViewSet, basename="product_category"
)

# Client
router.register("addresses", AddressViewSet, basename="address")
router.register("clients", ClientViewSet, basename="client")
router.register("users", UserViewSet, basename="user")

# Order
router.register("orders", OrderViewSet, basename="order")

# Product
router.register("additionals", AdditionalViewSet, basename="additional")
router.register("products", ProductViewSet, basename="product")


urlpatterns = [
    path("api/", include(router.urls)),  # API URLs
    path(
        "api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),  # JWT token obtain
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),  # JWT token refresh
]

# Include debug toolbar URLs.
if settings.DEBUG:
    urlpatterns += [
        path("admin/", admin.site.urls),  # Admin URLs
        path("api-auth/", include("rest_framework.urls")),  # REST framework auth URLs
        path(
            "api/token/verify/", TokenVerifyView.as_view(), name="token_verify"
        ),  # JWT token verify
        path(
            "swagger/", schema_view.with_ui("swagger"), name="schema-swagger-ui"
        ),  # Swagger UI
        path("redoc/", schema_view.with_ui("redoc"), name="schema-redoc"),  # ReDoc UI
    ]
    urlpatterns += debug_toolbar_urls()  # Debug toolbar URLs

# Include static URLs.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
