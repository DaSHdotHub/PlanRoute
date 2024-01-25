from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, AddressViewSet, DistanceViewSet, UserViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'distances', DistanceViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]   