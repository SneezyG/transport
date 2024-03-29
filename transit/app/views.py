from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from .models import Trip, Transporter, Payroll, User
from django.contrib.sessions.models import Session
from django.http import JsonResponse
import json
from datetime import datetime
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


channel_layer = get_channel_layer()




def Index(request):
  
   """
   return the transit-app index page with a link to the login interface.
   """
    
   template = "app/index.html"
   return render(request, template)








def Panel(request):
  
  """
  Check if user is logged in, then re-direct to a personalize view based on the user permissions.
  A user of manager user_type is redirected to the Monitor view.
  A user of supervisor user_type is redirected to the Manage view.
  A user of payroll user_type is redirected to the Pay view.
  A user of agent user_type is redirected to the the sync view in agent application.
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
  This return the the trip management panel, a personalize interface for supervisors.
  """
  
  template = "app/manage.html"
  user = request.user
  user_type = user.user_type
  user.session_key = request.session.session_key
  user.save()
  
  if user_type == "supervisor":
    trip_count = user.trips.filter(status="one").count()

    due_trips = user.trips.filter(status="one", due_date__lte=timezone.now())
    
    oneDay_trips = user.trips.filter(status="one", due_date__lte=timezone.now() + timezone.timedelta(days=1), due_date__gt=timezone.now())
    
    twoDays_trips = user.trips.filter(status="one", due_date__lte=timezone.now() + timezone.timedelta(days=2), due_date__gt=timezone.now() + timezone.timedelta(days=1))
    
    oneWeek_trips = user.trips.filter(status="one", due_date__lte=timezone.now() + timezone.timedelta(weeks=1), due_date__gt=timezone.now() + timezone.timedelta(days=2))
    
    twoWeeks_trips = user.trips.filter(status="one", due_date__lte=timezone.now() + timezone.timedelta(weeks=2), due_date__gt=timezone.now() + timezone.timedelta(weeks=1))
    
    oneMonth_trips = user.trips.filter(status="one", due_date__lte=timezone.now() + timezone.timedelta(weeks=4), due_date__gt=timezone.now() + timezone.timedelta(weeks=2))
    
    months_trips = user.trips.filter(status="one", due_date__gt=timezone.now() + timezone.timedelta(weeks=4))
    
  
    return render(request, template, {
      'due_trips': due_trips,
      'oneDay_trips': oneDay_trips,
      'twoDays_trips': twoDays_trips,
      'oneWeek_trips': oneWeek_trips,
      'twoWeeks_trips': twoWeeks_trips,
      'oneMonth_trips': oneMonth_trips,
      'months_trips': months_trips,
      'trip_count': trip_count,
    })
  raise PermissionDenied
  
 
 
 
 
 
 
 
 
def Monitor(request):
  
  """
  This return the the trip monitor panel, a personalize interface for the manager.
  """
  template = "app/monitor.html"
  user = request.user
  user_type = user.user_type
  is_super = user.is_superuser
  user.session_key = request.session.session_key
  user.save()
  
  if user_type == "manager" or is_super:
    due_trips = Trip.objects.filter(status="one", due_date__lte=timezone.now())
    
    oneDay_trips = Trip.objects.filter(status="one", due_date__lte=timezone.now() + timezone.timedelta(days=1), due_date__gt=timezone.now())
    
    twoDays_trips = Trip.objects.filter(status="one", due_date__lte=timezone.now() + timezone.timedelta(days=2), due_date__gt=timezone.now() + timezone.timedelta(days=1))
    
    oneWeek_trips = Trip.objects.filter(status="one", due_date__lte=timezone.now() + timezone.timedelta(weeks=1), due_date__gt=timezone.now() + timezone.timedelta(days=2))
    
    twoWeeks_trips = Trip.objects.filter(status="one", due_date__lte=timezone.now() + timezone.timedelta(weeks=2), due_date__gt=timezone.now() + timezone.timedelta(weeks=1))
    
    oneMonth_trips = Trip.objects.filter(status="one", due_date__lte=timezone.now() + timezone.timedelta(weeks=4), due_date__gt=timezone.now() + timezone.timedelta(weeks=2))
    
    months_trips = Trip.objects.filter(status="one", due_date__gt=timezone.now() + timezone.timedelta(weeks=4))
    
    return render(request, template, {
      'due_trips': due_trips,
      'oneDay_trips': oneDay_trips,
      'twoDays_trips': twoDays_trips,
      'oneWeek_trips': oneWeek_trips,
      'twoWeeks_trips': twoWeeks_trips,
      'oneMonth_trips': oneMonth_trips,
      'months_trips': months_trips,
    })
    
  raise PermissionDenied
  
  
  
  
  
  
  
  
  
  
def Welcome(request):
  
  """
  Return a welcome page after user authentication.
  """
  
  template = 'app/welcome.html'
  return render(request, template)
  
 
  
  
  
  
  
  
  

class Pay(View):
  
  """
  This return the payroll page on get request and a summary of closed-trips of a transporter from a specified date on post request.
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
    data = json.loads(request.body.decode('utf-8'))
    try:
      transporter = Transporter.objects.get(sn=data['id'])
    except Transporter.DoesNotExist:
      return JsonResponse({'error': 'invalid ID'}, status=400)
    
    trips = transporter.trips.filter(status="two", closed_date__gte=datetime(data['year'], data['month'], data['day']))
    
    if not trips:
      return JsonResponse({'error': 'transporter have no closed trips'}, status=400)
      
    photo = ''
    if transporter.photo:
      photo = transporter.photo.url
      
    short_trips = trips.filter(category="sh").count()
    mid_trips = trips.filter(category="md").count()
    long_trips = trips.filter(category="lg").count()
    
    payroll = Payroll.objects.all()[0]
    
    wages = (short_trips * payroll.short_range) + (mid_trips * payroll.mid_range) + (long_trips * payroll.long_range)
    total_trips = short_trips + mid_trips + long_trips
      
    return JsonResponse({
      'name': '%s %s' % (transporter.firstName, transporter.lastName), 
      'photo': photo,
      'short': short_trips,
      'mid': mid_trips,
      'long': long_trips,
      'sum': total_trips,
      'wages': wages
     })





def Tripclose(request, sn):
  """
   close a trip given a trip sn.
  """
  trip = Trip.objects.get(sn=sn)
  trip.status = "two"
  trip.closed_date = timezone.now()
  trip.save()
  return JsonResponse({'success': 'trip close successfully'})
  
  
  
def Tripupdate(request, sn, progress):
  """
   update a trip given a trip sn.
  """
  trip = Trip.objects.get(sn=sn)
  
  if trip.status == "two":
    return JsonResponse({'error': 'You are trying to update a closed trips'}, status=400)
    
  trip.progress = progress
  trip.save()
  
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
          "sn": sn,
          "progress": progress
        })
    except Exception as e:
      print(f"An error has occurred in the web-socket protocol: {e}")
  return JsonResponse({'success': 'trip updated successfully'})

