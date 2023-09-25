from django.shortcuts import render
from django.views import View
from django.core.exceptions import PermissionDenied

# Create your views here.


def Sync(request):
 
  """
  This return the syncTrip page of the agent app
  """
  
  template = 'agent/synctrip.html'
  user_type = request.user.user_type
  
  if user_type == "agent":
    return render(request, template)
  raise PermissionDenied
  
  
  
def Info(request):
  
  """
  This return the information page about a particular synced trip.
  """ 
  
  template = 'agent/info.html'
  user_type = request.user.user_type
  
  if user_type == "agent":
    return render(request, template)
  raise PermissionDenied



class Report(View):
  
  """
  This return the report page on get request and update trip report in the database on post request.
  """
  
  template = "agent/report.html"
  
  def dispatch(self, request, *args, **kwargs):
    user_type = request.user.user_type
    if user_type == "agent":
      return super().dispatch(request, *args, **kwargs)
    raise PermissionDenied
  
  def get(self, request, *args, **kwargs):
    return render(request, self.template)
    
    
  def post(self, request, *args, **kwargs):
    pass


