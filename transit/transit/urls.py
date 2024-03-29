"""mystore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/transit', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name="admin/login.html"), name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('', include(('app.urls', 'app'), namespace='app')),
    path('agent/', include(('agent.urls', 'agent'), namespace='agent')),
    path('^admin/', admin.site.urls),
    path('doc/', include('django.contrib.admindocs.urls')),
    path('admin/password_reset/', auth_views.PasswordResetView.as_view(),name='admin_password_reset',),
    path('admin/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done',),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm',),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete',),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
