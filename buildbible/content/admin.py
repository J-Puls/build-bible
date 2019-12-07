from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from django.contrib import admin
from .models import Post, ServiceManual
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'context', 'author', 'times_viewed', 'date_posted')
    list_filter = (('context', RelatedDropdownFilter), 'date_posted',)
    search_fields = ('title', 'description',)  
    empty_value_display = 'Not Specified'
    readonly_fields = ('author', 'times_viewed',)
class FsmAdmin(admin.ModelAdmin):
    list_display = ('display_filename','_model_name','_chassis_code', '_manufacturer', 'uploader', 'date_uploaded')
    list_filter = (('vehicle', RelatedDropdownFilter), ('uploader', RelatedDropdownFilter), 'date_uploaded',)
    search_fields = ('display_filename',)  
    def _model_name(self, profile):
        return profile.vehicle.model_name
    def _chassis_code(self, profile):
        return profile.vehicle.chassis_code
    def _manufacturer(self, profile):
        return profile.vehicle.manufacturer
    
    _model_name.admin_order_field = 'vehicle__model_name'
    _chassis_code.admin_order_field = 'vehicle__chassis_code'
    _manufacturer.admin_order_field = 'vehicle__manufacturer'

admin.site.register(Post, PostAdmin)
admin.site.register(ServiceManual, FsmAdmin)

admin.site.site_header = 'Build Bible Admin Dashboard'
