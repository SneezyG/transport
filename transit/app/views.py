from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection



# return the index page
def index(request):
  
   """
   return the transit-app index page with a link to the login interface.
   """
  
   return render(request, 'index.html')




# return the panel pages.
def panel(request):
  
  """
  Check if user is logged in, then check the user permissions and return a panel page build according to the amount of authority the user have.
  """
  
  return render(request, 'app/panel.html')
  
  
  
# return the welcome page after user authentication.
def welcome(request):
  
  """
  Check if user is authenticated and return a welcome page.
  """
  
  return render(request, 'app/welcome.html')

