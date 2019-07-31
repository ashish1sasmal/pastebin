from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Text(models.Model):
	topic=models.CharField(max_length=20)
	content=models.TextField()
	created_on=models.DateField()
	creator=models.ForeignKey(User,on_delete=models.CASCADE)

