from django.urls import path



from . import views



urlpatterns = [

  path('', views.sync, name='sync'),
  
]