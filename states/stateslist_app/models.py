from django.db import models

# Create your models here.

class State(models.Model):
  address = models.CharField(max_length=250)
  city = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  image = models.CharField(max_length=900)
  active = models.BooleanField(default=True)

  def __str__(self):
    return self.address