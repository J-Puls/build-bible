import json
from django.shortcuts import render, HttpResponse
from django.apps import apps
from django.core import serializers
from django.http import JsonResponse

Vehicle = apps.get_model('vehicles', 'Vehicle')
ServiceManual = apps.get_model('content', 'ServiceManual')
Post = apps.get_model('content', 'Post')

def update_choices(request):
    vehicle = request.GET.get('manufacturer')
    vehicle = Vehicle.objects.filter(manufacturer=vehicle).all()
    choices = []
    for v in vehicle:
        choices.append((v.id, v.model_name + ' (' + str(v.production_start) + '-' + str(v.production_end) + ')'))
    response_data = {}
    try:
        response_data['result'] = 'Success!'
        response_data['choices'] = choices
    except:
        response_data['result']= 'Error!'
        response_data['choices'] = 'Something went wrong...'
    response_data["Access-Control-Allow-Origin"] = "*"
    response_data["Access-Control-Allow-Methods"] = "GET"
    response_data["Access-Control-Max-Age"] = "1000"
    response_data["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def update_content(request):
    vehicle = request.GET.get('vehicle_id')
    category = request.GET.get('category')
    if int(vehicle) > 0:
        vehicle = Vehicle.objects.filter(id=vehicle).first()
    else:
        vehicle = None
    if int(category) > 0:
        if vehicle != []:
            posts = Post.objects.filter(context=vehicle).filter(category=category).all().values('id', 'title', 'description', 'date_posted')
        else:
            posts = Post.objects.filter(context=None).filter(category=category).all().values('id', 'title', 'description', 'date_posted')
        return JsonResponse(list(posts), safe=False)
    elif int(category) == 0:
        if vehicle != []:
            manuals = ServiceManual.objects.filter(vehicle=vehicle).order_by('display_filename').all().values('id', 'display_filename', 'date_uploaded', 'fsm_file')
            return JsonResponse(list(manuals), safe=False)
        else:
            return 'Not a valid request for general knowledge content.'

