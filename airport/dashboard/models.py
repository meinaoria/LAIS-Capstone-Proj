from django.db import models

class Elevator(models.Model):
	name = models.CharField(max_length=120, default='',blank = True, null=True)
	message = models.CharField(max_length=120, default='',blank = True, null=True)
	status = models.IntegerField(default=1,blank = True, null=True)
	last_update = models.DateTimeField(auto_now_add=True, auto_now=False)


class Escalator(models.Model):
	name = models.CharField(max_length=120, default='',blank = True, null=True)
	message = models.CharField(max_length=120, default='',blank = True, null=True)
	status = models.IntegerField(default=1,blank = True, null=True)
	last_update = models.DateTimeField(auto_now_add=True, auto_now=False)

class BaggageBelt(models.Model):
	name = models.CharField(max_length=120, default='',blank = True, null=True)
	message = models.CharField(max_length=120, default='',blank = True, null=True)
	status = models.IntegerField(default=1,blank = True, null=True)
	last_update = models.DateTimeField(auto_now_add=True, auto_now=False)