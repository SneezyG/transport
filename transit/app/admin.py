
from django.contrib import admin
from django.contrib.admin.models import LogEntry,DELETION
from django.utils.html import escape
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import User, Driver, Trip, Report, Message

# Register your models here.


# customized the admin interface
admin.site.empty_value_display = '(None)'
admin.site.list_per_page = 50
admin.site.site_header = 'Transit Data Store'
admin.site.index_title = "Data Store Management"
admin.site.site_title = "Data Admin"



@admin.register(User)
class UserAdmin(admin.modelAdmin):
  
    """
    Register the django Auth User model into the admin.
    Add some customization.
    """
    
    list_display = [
      'sn',
      'fullName',
      'username',
      'email',
      'address'
    ]
    


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    """
    Register the django log table into the admin.
    Add some customization and also define user access permission.
    """
    
    date_hierarchy = 'action_time'

    list_filter = [
        'user',
        'content_type',
        'action_flag',
        'action_time'
    ]


    search_fields = [
        'object_repr',
        'change_message'
    ]

    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_link',
        'action_flag',
    ]
    
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = '<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return mark_safe(link)
    object_link.admin_order_field = "object_repr"
    object_link.short_description = "object"
    
 
 
 
   
@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
  """
    Register the driver model into the admin.
    Add some customization.
  """
    
  fieldsets = (
    (None, {
      'classes': ('extrapretty'),
      'fields': (('firstName', 'middleName', 'lastName'), 'birthday', 'category', 'sex')
    }),
    
    ('Address', {
      'classes': ('extrapretty'),
      'fields': (('aptNo', 'laneNo'), 'street', ('city', 'state'), 'zipcode')
    }),
    )
    
  list_display = ('sn', 'fullName', 'category', 'address')
  
  list_filter = ('category', 'sex')
  
  preserve_filters = False

  search_fields = ['firstName', 'middleName', 'lastName']
  
