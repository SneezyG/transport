from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection



# return the index page
def index(request):
  
   """
   Query the recent company logo and return an HTML page with animated company logo and with a link to the login interface
   """
   
   try:
      # select company recently uploaded logo.
      with connection.cursor() as cursor:
        cursor.execute("SELECT logo FROM admin_interface_theme")
        path = cursor.fetchone()
        path = path[0]
        print(path)

   except:
      path = 0
  
   return render(request, 'app/index.html', {"logo": path})



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

