from django.shortcuts import render

# Create your views here.

# return the agent index page
def index(request):
 
  """
  This return the index page of the agent app and it's main function is to authenticate an agent.
  """
  
  return render(request, 'agent/index.html')


