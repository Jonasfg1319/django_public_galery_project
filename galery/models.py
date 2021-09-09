from django.db import models
import datetime
from datetime import timezone
# Create your models here.

class Images(models.Model):
  image_name = models.CharField(max_length=200)
  description = models.CharField(max_length=200)
  name_user = models.CharField(max_length=200)
  file = models.FileField(upload_to='galery/static/galery/img/')
  date = models.DateTimeField(auto_now=True)

  def __str__(self):
       return f"image_name: {self.image_name} -- description: {self.description}"

  def verify_field(self, str, str2):
      if(str[0] == " " or str2[0] == " "):
        return "empty"
      else:
       	return "fill"
  
  def verify_format(self,type):
      types = ["image/gif", "image/jpeg", "image/png"]
      permission = False
      for x in types:
        if(x == type):
          permission = True
          break
      return permission

  class Meta:
    ordering = ['-date']