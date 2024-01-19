from django.shortcuts import render
from .models import Patient

#Create your views here.
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})
