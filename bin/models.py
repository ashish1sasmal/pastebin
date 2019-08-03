from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.

print(User)

class Text(models.Model):
	topic=models.CharField(max_length=20)
	content=models.TextField()
	created_on=models.DateField()
	creator=models.ForeignKey(User,null=True,on_delete=models.CASCADE)

