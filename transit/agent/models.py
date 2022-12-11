
from django.db import models

# Create your models here.


class Agent(models.Model):
  
  """
  store a single agent data.
  """
  
  agent_name = models.CharField(max_length=30, unique=True)
  agent_pass = models.CharField(max_length=30)
  date = models.DateTimeField(auto_now_add=True)
  
  
  def __str__(self):
     return self.username


