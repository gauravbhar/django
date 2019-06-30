from django.db import models

# Create your models here.
class Reported(models.Model):
	full_name=models.CharField(max_length=70)
	def __str__(self):
		return self.full_name

class Article(models.Model):
	pub_date=models.DateField()
	headline=models.CharField(max_length=100)	
	content=models.CharField(max_length=200)
	rep_name=models.ForeignKey(Reported,on_delete=models.CASCADE)
	def __str__(self):
		return self.headline

