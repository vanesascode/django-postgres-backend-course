from django.db import models

class Business(models.Model):
  name = models.CharField(max_length=250)
  website = models.URLField(max_length=250)
  active = models.BooleanField(default=True)
  
  def __str__(self):
    return self.name

class State(models.Model):
  address = models.CharField(max_length=250)
  city = models.CharField(max_length=100)
  description = models.CharField(max_length=500)
  image = models.CharField(max_length=900)
  active = models.BooleanField(default=True)
  created = models.DateTimeField(auto_now_add=True)
  business = models.ForeignKey(Business, on_delete=models.CASCADE, related_name='stateslist')

  def __str__(self):
    return self.address
  
  # The on_delete=models.CASCADE argument specifies that if a Business instance is deleted, all associated State instances should also be deleted.
