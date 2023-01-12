from django.urls import path
from agent.views import Sync, Info, Report, Error
from django.contrib.auth.decorators import login_required




urlpatterns = [

  path('synctrip/', login_required(Sync), name='sync'),
  path('report/', login_required(Report.as_view()), name='report'),
  path('info/', login_required(Info), name='info'),
  path('error/', Error, name='error'),
  
]