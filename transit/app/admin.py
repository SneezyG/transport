
from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import User, Trip, Report, Booking, Payroll, Transporter
from django.contrib.auth.admin import UserAdmin

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

    




@admin.register(User)
class UserEntryAdmin(UserAdmin):
  
    """
    Register the User table into the admin.
    Add some customization.
    """
    
    date_hierarchy = 'date_joined'
    
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'office_line', 'personal_line', 'groups', 'user_permissions', 'is_active', 'is_staff', 'is_superuser', 'is_agent')}),
        )
    
    list_display = ('username', 'email', 'last_login', 'is_active', 'is_staff', 'is_superuser', 'is_agent', 'date_joined')
    
    list_filter = ('is_staff', 'is_active', 'is_superuser', 'is_agent', 'date_joined')
    
    preserve_filters = False

    search_fields = ('username',)




 
@admin.register(Transporter)  
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
    
  list_display = ('sn', 'fullName', 'address', 'date',)

  list_filter = ('sex', 'date')
  
  preserve_filters = False

  search_fields = ('sn', 'firstName', 'lastName')
  


   


@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
  
  """
  Register the Payroll model into the admin.
    Add some customization.
  """
  
  date_hierarchy = 'date'

  list_display = ("short_range", "mid_range", "long_range", "date")
  
  preserve_filters = False


  def has_add_permission(self, request):
    return False
  
  def has_change_permission(self, request, obj=None):
    return request.user.is_superuser

  def has_delete_permission(self, request, obj=None):
    return False

  def has_view_permission(self, request, obj=None):
    return request.user.is_superuser
  
  



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
  
  """
  Register the Booking model into the admin.
    Add some customization.
  """
  
  date_hierarchy = 'date'

  exclude = ('sn',)
  
  list_display = ('sn', 'name', 'booker', 'contact1', 'charges', 'paid', 'goods', 'pickup', 'delivery', 'date')
  
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
  
  autocomplete_fields = ('transporters', 'booking', 'management')




@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
  
  """
    Register the Report model into the admin.
    Add some customization and also define user access permission.
  """ 
  
  date_hierarchy = 'date'

  list_display = ('trip', 'status', 'progress', 'remark', 'date')

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
  

 