from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.exceptions import PermissionDenied
from app.models import Trip, Report
from django.http import Http404, JsonResponse
import json

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
  
  
  
def Info(request, sn):
  
  """
  This return the information page about a particular synced trip.
  """ 
  
  template = 'agent/info.html'
  user_type = request.user.user_type
  
  if user_type == "agent":
    trip = get_object_or_404(Trip, sn=sn)
    return render(request, template, {'trip': trip})
    
  raise PermissionDenied



class ReportView(View):
  
  """
  This return the report page on get request and update trip report in the database on post request.
  """
  
  template = "agent/report.html"
  
  def dispatch(self, request, *args, **kwargs):
    user_type = request.user.user_type
    if user_type == "agent":
      return super().dispatch(request, *args, **kwargs)
    raise PermissionDenied
  
  def get(self, request, sn, *args, **kwargs):
    trip = get_object_or_404(Trip, sn=sn)

    return render(request, self.template, {'trip': trip})
    
    
  def post(self, request, *args, **kwargs):
    data = json.loads(request.body.decode('utf-8'))
    try:
      trip = Trip.objects.get(sn=data['sn'])
    except Trip.DoesNotExist:
      return JsonResponse({'error': 'invalid trip ID'}, status=400)
      
    if trip.reports.count() == trip.report:
      return JsonResponse({'error': 'trip report exceeded'}, status=400)
    
    Report.objects.create(trip=trip, status=data["status"], progress=data["progress"], remark=["remark"])
    return JsonResponse({'success': 'report submitted successfully'})


