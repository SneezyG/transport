from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied




def Test(request):
  
   """
   return the transit-app index page with a link to the login interface.
   """
    
   template = "app/manage.html"
   return render(request, template)



def Index(request):
  
   """
   return the transit-app index page with a link to the login interface.
   """
    
   template = "app/index.html"
   return render(request, template)




def Panel(request):
  
  """
  Check if user is logged in, then re-direct to a specific view based on the user permissions.
  """
  
  user_type = request.user.user_type
  is_super = request.user.is_superuser
  
  if user_type == 'manager' or is_super:
    return HttpResponseRedirect(reverse('app:monitor'))
  elif user_type == 'agent':
    return HttpResponseRedirect(reverse('agent:sync'))
  elif user_type == 'supervisor':
    return HttpResponseRedirect(reverse('app:manage'))
  elif user_type == 'payroll':
    return HttpResponseRedirect(reverse('app:payroll'))
  else:
    raise PermissionDenied



def Manage(request):
  
  """
  This return the the management panel
  """
  
  template = "app/manage.html"
  user_type = request.user.user_type
  
  if user_type == "supervisor":
    return render(request, template)
  raise PermissionDenied
  
 
 
def Monitor(request):
  
  """
  This return the the monitor panel for the supervisor.
  """
  template = "app/monitor.html"
  user_type = request.user.user_type
  is_super = request.user.is_superuser
  
  if user_type == "manager" or is_super:
    return render(request, template)
  raise PermissionDenied
  
  
  
  
def Welcome(request):
  
  """
  Return a welcome page after user authentication.
  """
  
  template = 'app/welcome.html'
  return render(request, template)
  
 
  

class Payroll(View):
  
  """
  This return the payroll page on get request and query a trip summary of a freelancer on post request.
  """
  
  template = "app/payroll.html"
  
  def dispatch(self, request, *args, **kwargs):
    user_type = request.user.user_type
    if user_type == "payroll":
      return super().dispatch(request, *args, **kwargs)
    raise PermissionDenied
  
  def get(self, request, *args, **kwargs):
    return render(request, self.template)
    
    
  def post(self, request, *args, **kwargs):
    pass

