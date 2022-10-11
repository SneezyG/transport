
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import Driver, Mechanic, Loader, Trip, Report, Message, Booking, Payroll

# Register your models here.


# customized the admin interface
admin.site.empty_value_display = '(None)'
admin.site.list_per_page = 50
admin.site.site_header = 'Transit Data Store'
admin.site.index_title = "Data Store Management"
admin.site.site_title = "Data Admin"





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
        return False

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    
 
 
   
class TranspoterAdmin(admin.ModelAdmin):
  
  """
    This does not appear in the admin, it just provide an interface inherited by driverAdmin,
    mechanicAdmin and loaderAdmin.
  """
  
  date_hierarchy = 'date'

  fieldsets = (
    (None, {
      'classes': ('extrapretty'),
      'fields': (('sn', 'firstName', 'lastName'), 'birthday', 'phone', 'sex', 'photo')
    }),
    
    ('Address', {
      'classes': ('extrapretty'),
      'fields': (('aptNo', 'laneNo'), 'street', ('city', 'state', 'nationality'), 'zipcode')
    }),
    )
    
  list_display = ('sn', 'active', 'fullName', 'address', 'date',)

  list_filter = ('sex', 'active', 'date')
  
  preserve_filters = False

  search_fields = ('sn', 'firstName', 'lastName')
  

@admin.register(Driver)
class DriverAdmin(TranspoterAdmin):
   """
   This is subclass of TranspoterAdmin
   """
   pass
   
@admin.register(Mechanic)
class MechanicAdmin(TranspoterAdmin):
   """
   This is subclass of TranspoterAdmin
   """
   pass
  
@admin.register(Loader)
class MechanicAdmin(TranspoterAdmin):
   """
   This is subclass of TranspoterAdmin
   """  
   pass
  


@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
  
  """
  Register the Payroll model into the admin.
    Add some customization.
  """
  
  date_hierarchy = 'date'

  list_display = ("freelancer", "short_range", "mid_range", "long_range", "date")
  
  list_filter = ("freelancer",)
  
  preserve_filters = False
  
  

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
  
  """
  Register the Booking model into the admin.
    Add some customization.
  """
  
  date_hierarchy = 'date'

  exclude = ('sn',)
  
  list_display = ('sn', 'booker', 'contact', 'charges', 'paid', 'goods', 'pickup', 'delivery', 'date')
  
  list_filter = ("paid", "date")
  
  preserve_filters = False

  search_fields = ('sn', 'booker')
   
   
    
@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
  
  """
    Register the Trip model into the admin.
    Add some customization.
  """ 
  
  date_hierarchy = 'date'
  
  exclude = ('sn',)
  
  list_display = ('sn', 'booking', 'category', 'management', 'report', 'status', 'progress', 'date')
  
  list_filter = ('category', 'status', 'progress', 'date',)
  
  preserve_filters = False

  search_fields = ('sn',)
  
  autocomplete_fields = ('drivers', 'mechanics', 'loaders', 'management')




@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
  
  """
    Register the Report model into the admin.
    Add some customization and also define user access permission.
  """ 
  
  date_hierarchy = 'date'

  list_display = ('trip', 'status', 'remark', 'coord', 'date')

  list_filter = ('status', 'date',)
  
  preserve_filters = False

  search_fields = ('trip__sn',)
  
  
  def has_add_permission(self, request):
        return False

  def has_change_permission(self, request, obj=None):
        return False

  def has_delete_permission(self, request, obj=None):
        return False

  def has_view_permission(self, request, obj=None):
        return request.user.is_superuser
  

  


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
  
  """
    Register the Message model into the admin.
    Add some customization and also define user access permission.
  """ 
  
  date_hierarchy = 'date'

  list_display = ('trip', 'message', 'label', 'status', 'date')

  list_filter = ('label', 'status', 'date',)
  
  preserve_filters = False

  search_fields = ('trip__sn',)
  
  
  def has_add_permission(self, request):
        return False

  def has_change_permission(self, request, obj=None):
        return False

  def has_delete_permission(self, request, obj=None):
        return False

  def has_view_permission(self, request, obj=None):
        return request.user.is_superuser
