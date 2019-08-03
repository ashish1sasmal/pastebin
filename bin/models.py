from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Text(models.Model):
	topic=models.CharField(max_length=20)
	content=models.TextField()
	created_on=models.DateTimeField(auto_now_add=True,blank=True)
	creator=models.ForeignKey(User,null=True,on_delete=models.CASCADE,editable=False)

