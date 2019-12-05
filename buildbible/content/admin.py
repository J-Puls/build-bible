from django_admin_listfilter_dropdown.filters import DropdownFilter, RelatedDropdownFilter, ChoiceDropdownFilter
from django.contrib import admin
from .models import Post, ServiceManual
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'context', 'author', 'date_posted')
    list_filter = (('context', RelatedDropdownFilter), 'date_posted',)
    search_fields = ('title', 'description',)  
    empty_value_display = 'Not Specified'
    
class FsmAdmin(admin.ModelAdmin):
    list_display = ('display_filename', 'vehicle', 'uploader', 'date_uploaded')
    list_filter = (('vehicle', RelatedDropdownFilter), ('uploader', RelatedDropdownFilter), 'date_uploaded',)
    search_fields = ('display_filename',)  


admin.site.register(Post, PostAdmin)
admin.site.register(ServiceManual, FsmAdmin)

admin.site.site_header = 'Build Bible Admin Dashboard'
