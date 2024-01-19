from django.urls import path
from .views import patient_list

urlpatterns = [
    # ... other url patterns ...
    path('', patient_list, name='patient-list'),
]
