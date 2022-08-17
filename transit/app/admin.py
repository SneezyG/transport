
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import User, Driver, Trip, Report, Message
from .form import TripAdminForm

# Register your models here.


# customized the admin interface
admin.site.empty_value_display = '(None)'
admin.site.list_per_page = 50
admin.site.site_header = 'Transit Data Store'
admin.site.index_title = "Data Store Management"
admin.site.site_title = "Data Admin"



@admin.register(User)
class UserAdmin(admin.ModelAdmin):
  
    """
    Register the django Auth User model into the admin.
    Add some customization.
    """
    
    date_hierarchy = 'date_joined'
    
    fieldsets = (
    (None, {
      'classes': ('extrapretty'),
      'fields': ('username', 'first_name', 'last_name', 'phone', 'email', 'password', 'photo', 'birthday', 'sex', 'groups', 'user_permissions', 'is_active', 'is_staff', 'is_superuser')
    }),
    
    ('Address', {
      'classes': ('extrapretty'),
      'fields': (('aptNo', 'laneNo'), 'street', ('city', 'state'), 'zipcode')
    }),
    )
    
    list_display = [
      'sn',
      'fullName',
      'username',
      'email',
      'address',
      'date_joined',
    ]
    
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'date_joined')
    
    preserve_filters = False
    
    search_fields = ('username', 'first_name', 'last_name')
    


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

    
 
 
   
@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
  
  """
    Register the driver model into the admin.
    Add some customization.
  """
  
  date_hierarchy = 'date'

  fieldsets = (
    (None, {
      'classes': ('extrapretty'),
      'fields': (('firstName', 'lastName'), 'birthday', 'phone', 'category', 'sex', 'photo')
    }),
    
    ('Address', {
      'classes': ('extrapretty'),
      'fields': (('aptNo', 'laneNo'), 'street', ('city', 'state'), 'zipcode')
    }),
    )
    
  list_display = ('sn', 'fullName', 'category', 'address', 'date',)

  list_filter = ('category', 'sex', 'date',)
  
  preserve_filters = False

  search_fields = ['firstName', 'lastName']
  


    
@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
  
  """
    Register the Trip model into the admin.
    Add some customization.
  """ 
  
  date_hierarchy = 'date'

  form = TripAdminForm
  
  exclude = ('sn',)
  
  list_display = ('sn', 'origin', 'destination', 'address', 'category', 'driver', 'management', 'report', 'status', 'date')
  
  list_filter = ('category', 'status', 'date',)
  
  preserve_filters = False

  search_fields = ('origin', 'destination', 'address',)
  
  autocomplete_fields = ('driver', 'management',)




@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
  
  """
    Register the Report model into the admin.
    Add some customization.
  """ 
  
  date_hierarchy = 'date'

  list_display = ('trip', 'status', 'comment', 'location', 'coord', 'date')

  list_filter = ('status', 'date',)
  
  preserve_filters = False

  search_fields = ('trip__sn',)

  autocomplete_fields = ('trip',)

  


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
  
  """
    Register the Message model into the admin.
    Add some customization.
  """ 
  
  date_hierarchy = 'date'

  list_display = ('trip', 'message', 'label', 'status', 'date')

  list_filter = ('label', 'status', 'date',)
  
  preserve_filters = False

  search_fields = ('trip__sn',)
  
  autocomplete_fields = ('trip',)