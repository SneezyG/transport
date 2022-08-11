
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid



def path(instance, filename):
  return 'driver/driver_{0}/{1}'.format(instance.sn, filename)
  
def location(instance, filename):
  return 'user/user_{0}/{1}'.format(instance.sn, filename)



class User(AbstractUser):
  
  """
  Stores a single user data.
  extend the dafault django auth user modelling
  """
  
  sexType = (
      ('M', 'male'),
      ('F', 'female'),
      ('P', 'private'),
    )
  
  sn = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='id')
  photo = models.ImageField(upload_to=location, null=True, blank=True)
  birthday = models.DateField()
  phone = models.CharField(max_length=15)
  sex = models.CharField(max_length=1, choices=sexType)
  aptNo = models.IntegerField(verbose_name='apartment number')
  laneNo = models.IntegerField(verbose_name='lane number')
  street = models.CharField(max_length=30)
  city = models.CharField(max_length=30)
  state = models.CharField(max_length=30,)
  zipcode = models.IntegerField()
  
  
  def fullName(self):
    "Returns the person's full name."
    verbose_name='full name'
    fullname = '%s %s' % (self.first_name, self.last_name)
    return fullname.upper()
    
    
  def __str__(self):
    fullname = '%s %s' % (self.first_name, self.last_name)
    return fullname.title()
    
 
  def address(self):
    "Return the address of the person."
    address = 'no %s, lane %s, %s, %s, %s' % (self.aptNo, self.laneNo, self.street, self.city, self.state)
    return address.title()

 
 
 
  
class Driver(models.Model):
  
  """
  Stores a single driver data.
  
  There are two category of Driver(full-time and part-time)
  
  """
  
  sexType = (
      ('M', 'male'),
      ('F', 'female'),
      ('P', 'private'),
    )
    
  driverType= (
      ("PT", "Full-time"),
      ("FT", "Part-time"),
    )

    
  sn = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name='id')
  firstName = models.CharField(max_length=30, verbose_name='first name')
  lastName = models.CharField(max_length=30, verbose_name='last name')
  birthday = models.DateField()
  photo = models.ImageField(upload_to=path, null=True, blank=True)
  category = models.CharField(max_length=4,
      choices=driverType)
  sex = models.CharField(max_length=1, choices=sexType)
  aptNo = models.IntegerField(verbose_name='apartment number')
  phone = models.CharField(max_length=15)
  laneNo = models.IntegerField(verbose_name='lane number')
  street = models.CharField(max_length=30)
  city = models.CharField(max_length=30)
  state = models.CharField(max_length=30,)
  zipcode = models.IntegerField()
  
 

  def fullName(self):
    "Returns the person's full name."
    verbose_name='full name'
    fullname = '%s %s' % (self.firstName, self.lastName)
    return fullname.upper()
    
    
  def __str__(self):
    fullname = '%s %s(%s)' % (self.firstName, self.lastName, self.category)
    return fullname.title()
    
 
  def address(self):
    "Return the address of the person."
    address = 'no %s, lane %s, %s, %s, %s' % (self.aptNo, self.laneNo, self.street, self.city, self.state)
    return address.title()




class Trip(models.Model):
  
  """
  Stores a single trip data.
  
  There are three category of trip(interstate, intrastate and cross-country).
  
  It is related to the drivers and management through a ForeignKey relationship.

  Admin also known as superuser can't assign to a trip.
  
  """
  
  catgType = (
     ("inter", "Interstate"),
     ("intra", "Intrastate"),
     ("cross", "Cross-country")
  )
  
  statusType = (
     ("Cl", "Close"),
     ("Op", "Open")
  )
  
  sn = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name="id")
  origin = models.CharField(max_length=50, default="station")
  destination = models.CharField(max_length=50)
  address = models.CharField(max_length=200, verbose_name="destination address")
  category = models.CharField(max_length=7, choices=catgType)
  driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, related_name='trips')
  management = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='trips')
  report_cnt = models.IntegerField(verbose_name='Expected report')
  status = models.CharField(max_length=5, choices=statusType)
  date = models.DateField(auto_now_add=True)
  
  
  def __str__(self):
    fullname = '%s (%s-%s)' % (self.ssn, self.origin, self.destination)
    return fullname.title()
    
    
  # over ride the save method
  def save(self, *args, **kwargs):
    if not self.management.is_superuser:
      super().save(*args, **kwargs) 
    else:
      return "Admin can't be assign to a trip"
  
  


class Report(models.Model):
  
  """
  Stores a single report data.
  
  A report is related to the trip table through a foreign key relationship
  
  """
  
  statusType = (
     ('G', 'Green'),
     ('R', 'Red'),
     ('Y', 'Yellow')
  )
  
  trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='reports')
  status = models.CharField(max_length=5, choices=statusType)
  comment = models.TextField()
  location = models.CharField(max_length=50)
  coord = models.CharField(max_length=200)
  date = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    rep = '%s (%s)' % (self.comment, self.status)
    return rep.title()
  
 

  
class Chat(models.Model):
  
  """
  Stores a single chat history.
  A chat is related to the trip table through a OneToOneField relationship
  """
  
  trip = models.OneToOneField(Trip, on_delete=models.CASCADE, related_name='chat')
  date = models.DateField(auto_now_add=True)
  
  
  
 
 
class Message(models.Model):
  
  """
  store a single message data.
  
  A message is related to the chat table through a foreign key relationship.
  """
  
  labelType = (
    ('D', 'Driver'), 
    ('M', 'Management')
  )
 
  statusType = (
    ('S', 'send'),
    ('D', 'delivered'),
    ('R', 'read')
  )
 
  message = models.TextField()
  chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
  label = models.CharField(max_length=5, choices=labelType)
  status = models.CharField(max_length=5, choices=statusType)
  date = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    rep = '%s (%s)' % (self.message, self.status)
    return rep.title()
    
