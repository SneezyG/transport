from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.exceptions import PermissionDenied
from app.models import Trip, Report, User
from django.http import Http404, JsonResponse
from django.contrib.sessions.models import Session
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()

# Create your views here.


def Sync(request):
 
  """
  This return the syncTrip page of the agent app, which is used for syncing of trips before they can depart.
  """
  
  template = 'agent/synctrip.html'
  user_type = request.user.user_type
  
  if user_type == "agent":
    return render(request, template)
  raise PermissionDenied
  
  
  
def Info(request, sn):
  
  """
  This return the info page containing information about a particular synced trip.
  """ 
  
  template = 'agent/info.html'
  user_type = request.user.user_type
  
  if user_type == "agent":
    trip = get_object_or_404(Trip, sn=sn)
    return render(request, template, {'trip': trip})
    
  raise PermissionDenied



class ReportView(View):
  
  """
  This return the report page on get request, which is use for updating trip reports in the database on post request.
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
      
    if trip.reports.count() >= trip.report:
      return JsonResponse({'error': 'trip report exceeded'}, status=400)
      
    if trip.status == "two": 
      return JsonResponse({'error': 'trip already closed'}, status=400)
    
    report = Report.objects.create(trip=trip, status=data["status"], progress=data["progress"], remark=data["remark"], longitude=data["long"], latitude=data["lat"])
    trip.latest_report = report
    trip.save()
    
    try:
      key = trip.management.session_key
      session = Session.objects.get(session_key=key)
      session_data = session.get_decoded()
      channel_name = session_data.get('channel_name')
      if channel_name:
        data["created"] = str(report.date)
        data["Expected_report"] = trip.report
        data["report_count"] = trip.reports.count()
        data["type"] = "chat.message"
        async_to_sync(channel_layer.send)(channel_name, data)
    except Exception as e:
       print(f"An error has occurred in the web-socket protocol: {e}")
       
    users = User.objects.filter(is_superuser=True)
    for user in users:
      key = user.session_key
      try:
        session = Session.objects.get(session_key=key)
        session_data = session.get_decoded()
        channel_name = session_data.get('channel_name')
        if channel_name:
          async_to_sync(channel_layer.send)(channel_name, {
            "type": "chat.message",
            "sn": data['sn'],
            "status": data['status']
          })
      except Exception as e:
        print(f"An error has occurred in the web-socket protocol: {e}")

    return JsonResponse({'success': 'report submitted successfully'})


