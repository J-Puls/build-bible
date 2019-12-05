from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Vehicle, VehicleProfile

def vehicle(request):
    chosen_vehicle = request.GET.get('vehicle')
    context={
        'vehicle': VehicleProfile.objects.filter(vehicle_id=chosen_vehicle).first(),
    }
    return render(request, 'vehicles/vehicle.html', context)