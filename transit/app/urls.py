from django.urls import path
from django.contrib.auth.decorators import login_required
from app.views import Index, Panel, Manage, Monitor, Welcome, Pay, Tripclose, Tripupdate



urlpatterns = [

  path('', Index, name='index'),
  path('welcome/', login_required(Welcome), name='welcome'),
  path('panel/', login_required(Panel), name='panel'),
  path('manage/', login_required(Manage), name='manage'),
  path('monitorTrip/', login_required(Monitor), name='monitor'),
  path('payroll/', login_required(Pay.as_view()), name='payroll'),
  path('tripclose/<str:sn>/', login_required(Tripclose), name='tripclose'),
  path('tripupdate/<str:sn>/<str:no>/', login_required(Tripupdate), name='tripupdate'),
  
]