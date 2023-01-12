from django.shortcuts import render
from django.views import View

# Create your views here.


def Sync(request):
 
  """
  This return the syncTrip page of the agent app
  """
  
  template = 'agent/synctrip.html'
  return render(request, template)
  
  
  
def Info(request):
  
  """
  This return the information page about a particular synced trip.
  """ 
  
  template = 'agent/info.html'
  return render(request, template)



class Report(View):
  
  """
  This return the report page on get request and update trip report in the database on post request.
  """
  
  template = "agent/report.html"
  
  def get(self, request, *args, **kwargs):
    return render(request, self.template) 
    
    
  def post(self, request, *args, **kwargs):
    pass




def Error(request):
  template = '500.html'
  return render(request, template)
