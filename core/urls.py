from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, AddressViewSet, DistanceViewSet, UserViewSet
import os

schema_view = get_schema_view(
    openapi.Info(
        title="PlanRoute API",
        default_version="v1",
        description="API for PlanRoute",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'addresses', AddressViewSet, basename='address')
router.register(r'distances', DistanceViewSet,  basename='distance')
router.register(r'users', UserViewSet, basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]

# Add the Swagger and Redoc documentation for the API in development mode
dev_mode = os.getenv("DEVELOPMENT", "False") == "True"
if dev_mode:
    urlpatterns += [
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]   