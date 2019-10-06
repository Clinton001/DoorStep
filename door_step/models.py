from django.db import models
from django.utils import timezone
# Create your models here.

class Package_Tracking(models.Model):
	tracking_number	=	 models.CharField(max_length=20)
	Receiver_Last_Name		=	models.CharField(max_length=20)
	Service_Type	=	 models.CharField(max_length=50)
	Date_Time		=	models.DateTimeField(default=timezone.now)
	Package_status	 		= 	models.TextField()
	Sender_Name			=	models.CharField(max_length=50)
	Billng_Activity		=	models.TextField()
	Current_Location		=	models.TextField()
	Payment_Details			=	models.TextField()
	Receiver_Address	=	models.TextField()
	Estimated_delivery	=	models.DateTimeField(default=timezone.now)
	Ship_date			=	models.DateTimeField(default=timezone.now)
