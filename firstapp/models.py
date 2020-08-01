from django.db import models
class Registration(models.Model):
	name=models.CharField(max_length=20)
	password=models.CharField(max_length=10)
	class Meta:
		db_table="Registration"
	def __str__(self):
		return self.name


# Create your models here.
