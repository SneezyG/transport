from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse




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
  
  user = request.user
  
  if user.is_superuser:
    return HttpResponseRedirect(reverse('app:monitor'))
  elif user.is_agent:
    return HttpResponseRedirect(reverse('agent:sync'))
  else:
    return HttpResponseRedirect(reverse('app:manage'))



def Manage(request):
  
  """
  This return the the management panel
  """
  
  template = "app/manage.html"
  return render(request, template)
  
 
 
def Monitor(request):
  
  """
  This return the the monitor panel for the supervisor.
  """
  template = "app/monitor.html"
  return render(request, template)
  
  
  
  
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
  
  def get(self, request, *args, **kwargs):
    return render(request, self.template) 
    
    
  def post(self, request, *args, **kwargs):
    pass

