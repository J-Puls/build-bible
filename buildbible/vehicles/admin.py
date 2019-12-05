from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from django.contrib import admin
from .models import Vehicle, VehicleProfile


class VehicleAdmin(admin.ModelAdmin):
    list_filter = (('manufacturer', ChoiceDropdownFilter), 'model_name',)
    list_display = ('model_name', 'chassis_code', 'manufacturer', 'production_start', 'production_end',)
    ordering = ['manufacturer', 'model_name', 'production_start']
    search_fields = ('manufacturer', 'model_name', 'chassis_code','production_start', 'production_end',) 


class VehicleProfileAdmin(admin.ModelAdmin):
    list_display = ('vehicle',)
    list_filter = (('vehicle', RelatedDropdownFilter),)

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleProfile, VehicleProfileAdmin)
