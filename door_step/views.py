from django.shortcuts import render
from django.views.generic import ListView
from .models import Package_Tracking

# Create your views here.





def home_view(request):

	return render(request, "door_step/Home.html", {})



def about_view(request):

	return render(request, "door_step/About.html", {})


def services_view(request):

	return render(request, "door_step/Services.html", {})


def contact_view(request):

	return render(request, "door_step/Contact.html", {})

def track_view(request):


	return render(request, "door_step/Track.html", {})


#Package class, control every view seen in the package
class package_details(ListView):

	model = Package_Tracking
	template_name =  "door_step/Package_details.html"
	context_object_name = "track_details"

	
	

def loader(request):

	return render(request, "door_step/loader.html", {})