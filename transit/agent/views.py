from django.shortcuts import render

# Create your views here.

# return the agent syncTrip page.
def sync(request):
 
  """
  This return the syncTrip page of the agent app and it's main function is to sync a trip into the agent application.
  """
  
  return render(request, 'agent/synctrip.html')


