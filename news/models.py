from django.db import models

# Create your models here.
class New(models.Model):
	new_title=models.CharField(max_length=300)
	new_date=models.DateTimeField()
	new_url=models.CharField(max_length=300)