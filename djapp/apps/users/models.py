from django.db import models



class petition(models.Model):
	user 		= models.CharField(max_length=255)
	track 		= models.CharField(max_length=255)
	artist		= models.CharField(max_length=255,null=True,blank=True)
	url			= models.URLField(max_length=255,verify_exists=True,null=True,blank=True)
	video_url 	= models.URLField(max_length=255,verify_exists=True,null=True,blank=True)
	date		= models.DateTimeField(auto_now=True)
	status 		= models.BooleanField(default=True)






