from django.urls import path
from agent.views import Sync, Info, ReportView
from django.contrib.auth.decorators import login_required




urlpatterns = [

  path('synctrip/', login_required(Sync), name='sync'),
  path('report/<str:sn>/', login_required(ReportView.as_view()), name='report'),
  path('info/<str:sn>/', login_required(Info), name='info'),
  
]