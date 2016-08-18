from django.db import models
# Create your models here.

class day(models.Model):
# Create your models here.
	date=models.DateField(auto_now_add=True)
	starttime=models.TimeField()
	t1=models.CharField(max_length=200)
	t2=models.CharField(max_length=200)
	t3=models.CharField(max_length=200)
	t4=models.CharField(max_length=200)
	t5=models.CharField(max_length=200)
	t6=models.CharField(max_length=200)
	t7=models.CharField(max_length=200)
	t8=models.CharField(max_length=200)
	t9=models.CharField(max_length=200)
	t10=models.CharField(max_length=200)
	t11=models.CharField(max_length=200)
	t12=models.CharField(max_length=200)
	t13=models.CharField(max_length=200)
	t14=models.CharField(max_length=200)
	t15=models.CharField(max_length=200)
	t16=models.CharField(max_length=200)
	def __str__(self):
		return self.t1

		
class task(models.Model):
	text=models.CharField(max_length=200)
	topbranch=models.CharField(max_length=200)
	next=models.CharField(max_length=200)
	previous=models.CharField(max_length=200)
	startdate=models.DateField()
	completedate=models.DateField()
	progressvalue=models.IntegerField(default=0)
	audio = models.FileField(upload_to='goal/media', blank=True)
	def __str__(self):
		return self.text