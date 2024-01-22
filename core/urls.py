from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, AddressViewSet, DistanceViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'distances', DistanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]   