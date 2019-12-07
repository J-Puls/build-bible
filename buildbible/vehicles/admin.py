from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from django.contrib import admin
from .models import Vehicle, VehicleProfile


class VehicleAdmin(admin.ModelAdmin):
    list_filter = (('manufacturer', ChoiceDropdownFilter), 'model_name',)
    list_display = ('model_name', 'chassis_code', 'manufacturer', 'production_start', 'production_end',)
    ordering = ['manufacturer', 'model_name', 'production_start']
    search_fields = ('manufacturer', 'model_name', 'chassis_code','production_start', 'production_end',) 


class VehicleProfileAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ('_model_name', '_chassis_code', '_manufacturer',)

    def _model_name(self, profile):
        return profile.context.model_name
    def _chassis_code(self, profile):
        return profile.context.chassis_code
    def _manufacturer(self, profile):
        return profile.context.manufacturer
    
    _model_name.admin_order_field = 'context__model_name'
    _chassis_code.admin_order_field = 'context__chassis_code'
    _manufacturer.admin_order_field = 'context__manufacturer'
    
    fields = ('image_tag', 'image',)
    readonly_fields = ('image_tag',)

admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleProfile, VehicleProfileAdmin)
