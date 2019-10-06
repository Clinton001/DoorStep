from django.urls import path
from door_step import views
from .views import package_details

urlpatterns = [
    path('', views.home_view, name="Home"),
    path('about/', views.about_view, name="About"),
 	path('services/', views.services_view, name="Services"),
 	path('contact/', views.contact_view, name="Contact"),
 	path('track/', views.track_view, name="Track"),
 	path('track/package/', package_details.as_view(), name="Package"),
 	path('track/checking', views.loader, name="checking"),
   
] 
