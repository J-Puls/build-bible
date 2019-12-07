from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Vehicle, VehicleProfile

def vehicle(request):
    chosen_vehicle = request.GET.get('vehicle')
    context={
        'v_profile': VehicleProfile.objects.filter(context_id=chosen_vehicle).first(),
    }
    return render(request, 'vehicles/vehicle.html', context)