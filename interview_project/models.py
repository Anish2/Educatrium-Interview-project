from django.db import models
import random


# Create your models here.
class Element(models.Model):	
	element_id = models.IntegerField(default = 0, unique=True)
	random_header = models.CharField(max_length = 200)
	random_text = models.CharField(max_length = 200)
	random_popup_title = models.CharField(max_length = 200)
	random_popup_text = models.CharField(max_length = 1000)
	def __str__(self):
		return self.random_header