"""ofipensiones URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import include, path
from django.contrib.auth import logout
from django.shortcuts import redirect
from . import views

# # Funciones para manejar logout
# def logout_view(request):
#     logout(request)  # Cierra sesión en Django
#     return redirect('logout_auth0')  # Redirige a Auth0 para cerrar sesión global

# def logout_auth0(request):
#     domain = 'dev-58o2d2rv00kn78f5.us.auth0.com'  # Cambia por tu dominio Auth0
#     client_id = 'kJfxxY2ndiUaAoKSCaPHOvMKTpg59C5C'  # Reemplaza con tu Client ID de Auth0
#     return_to = 'http://localhost:8000/'  # Página a la que redirigir después del logout
#     logout_url = f"https://dev-58o2d2rv00kn78f5.us.auth0.com/v2/logout?returnTo=http%3A%2F%2Flocalhost"
#     return redirect(logout_url)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('health-check/', views.healtCheck),
    path('pagos/', include('pagos.urls')),
    path('cuenta/', include('cuenta.urls')),
    path('responsableEconomico/', include('responsableEconomico.urls')),
    path('cobros/', include('cobro.urls')),
    path('descuentos/', include('descuento.urls')),
    path('usuarios/', include('usuario.urls')),  
    path('reportes/', include('reportes.urls')),    
    path(r'', include('django.contrib.auth.urls')),
    path(r'', include('social_django.urls')),
    
    #path('logout/', logout_view, name='logout'),  # Ruta para logout de Django
    #path('logout_auth0/', logout_auth0, name='logout_auth0'),  # Logout Auth0


]
