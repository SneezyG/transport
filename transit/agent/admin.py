
from django.contrib import admin
from .models import Agent

# Register your models here.


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    """
    Register the User table into the admin.
    Add some customization.
    """
    
    date_hierarchy = 'date'
    
    list_display = ('agent_name', 'date')
    
    list_filter = ('date',)
    
    preserve_filters = False

    search_fields = ('agent_name',)
    
    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser
  
