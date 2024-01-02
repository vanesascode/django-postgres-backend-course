from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

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
  
class Comment(models.Model):
    score = models.PositiveIntegerField(
    validators=[MinValueValidator(1), MaxValueValidator(5)])
    texto = models.CharField(max_length=200, null=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='comments')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    
    def __str__(self) :
      return str(self.score) + ' ' + self.state.address
  
  
  # The on_delete=models.CASCADE argument specifies that if a Business instance is deleted, all associated State instances should also be deleted.
