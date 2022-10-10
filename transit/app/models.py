
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
import uuid



def driv(instance, filename):
  #create a unique path for drivers photo.
  return 'driver_{0}/{1}'.format(instance.id, filename)

def mech(instance, filename):
  #create a unique path for mechanics photo.
  return 'mechanic_{0}/{1}'.format(instance.id, filename)
  
def load(instance, filename):
  #create a unique path for loaders photo.
  return 'loader_{0}/{1}'.format(instance.id, filename)

def doc1(instance, filename):
  #create a unique path for doc1.
  return 'doc1_{0}/{1}'.format(instance.id, filename)
  
def doc2(instance, filename):
  #create a unique path for doc2.
  return 'doc2_{0}/{1}'.format(instance.id, filename)
  
def flip(obj, active):
  # flip transporters active status.
  for x in obj:
    x.active = active
    x.save()
    
def castValidator(value):
   try:
     float(value)
   except:
     error = "only decimal and integer is valid for this field"
     raise ValidationError(error)
      
 
 
 
  
class Transporter(models.Model):
  
  """
  This model is a generalisation of Driver, Mechanic and Loader model.
  Transporters are freelancers which are paid based on the type and amount of trip they go.
  """
  
  sexType = (
      ('M', 'male'),
      ('F', 'female'),
      ('P', 'private'),
    )
    
  
  sn = models.CharField(max_length=30, unique=True, verbose_name='id')
  firstName = models.CharField(max_length=30, verbose_name='first name')
  lastName = models.CharField(max_length=30, verbose_name='last name')
  birthday = models.DateField()
  sex = models.CharField(max_length=1, choices=sexType)
  phone = models.CharField(max_length=15)
  photo = models.ImageField()
  aptNo = models.IntegerField(verbose_name='apartment number')
  laneNo = models.IntegerField(verbose_name='lane number')
  street = models.CharField(max_length=30)
  city = models.CharField(max_length=30)
  state = models.CharField(max_length=30,)
  zipcode = models.IntegerField()
  active = models.BooleanField(default=False)
  date = models.DateTimeField(auto_now_add=True)
  
 

  def fullName(self):
    "Returns the person's full name."
    verbose_name='full name'
    fullname = '%s %s' % (self.firstName, self.lastName)
    return fullname.upper()
    
    
  def __str__(self):
    text = '%s %s(active: %s)' % (self.firstName, self.lastName, self.active)
    return text.title()
    
 
  def address(self):
    "Return the address of the person."
    address = 'no %s, lane %s, %s, %s, %s' % (self.aptNo, self.laneNo, self.street, self.city, self.state)
    return address.title()


class Driver(Transporter):
  """
  Stores a single driver data.
  This is specialization of Transporter model.
  """
  photo = models.ImageField(upload_to=driv)

class Mechanic(Transporter):
  """
  Stores a single Mechanic data.
  This is specialization of Transporter model.
  """
  photo = models.ImageField(upload_to=mech)
  
class Loader(Transporter):
  """
  Stores a single Loader data.
  This is specialization of Transporter model.
  """
  photo = models.ImageField(upload_to=load)
  
  


class Payroll(models.Model):
  """
  This is rather a simple model to persist the amount paid per trip to freelancer transporters.
  The amount pay per trip depend on the category of transporter and type of trip
  """
 freeType = (
   ("driv", "Driver"),
   ("mech", "Mechanic"),
   ("load", "Loader")
 )
 
 freelancer = models.CharField(max_length=5, choices=freeType)
 short_range = models.CharField(max_length=30, verbose_name="pay/short-range trip in $", validators=[castValidator])
 mid_range = models.CharField(max_length=30, verbose_name="pay/mid-range trip in $", validators=[castValidator])
 long_range = models.CharField(max_length=30, verbose_name="pay/long-range trip in $", validators=[castValidator])
 date = models.DateTimeField(auto_now=True)
 
 
 def __str__(self):
    text = '%s(goods: %s)' % (self.booker, self.goods)
    return text.title()
    
 



class Booking(models.model):
  """
  Stores a single trip-booking data.
  This model also includes two file field to store important bookings documents.
  """
  sn = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name="id")
  booker = models.CharField(max_length=30, verbose_name="Booker's name")
  contact = models.CharField(max_length=15, verbose_name="Booker's contact")
  charges = models.CharField(max_length=30, verbose_name="Amount due", validators=[castValidator])
  paid = models.BooleanField(default=False)
  goods = models.CharField(max_length=30)
  pickup = models.CharField(max_length=100, verbose_name="pickup address")
  delivery = models.CharField(max_length=100, verbose_name="delivery address")
  doc1 = models.FileField(upload_to=doc1, null=True, blank=True)
  doc2 = models.FileField(upload_to=doc2, null=True, blank=True)
  date = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    text = '%s(goods: %s)' % (self.booker, self.goods)
    return text.title()




class Trip(models.Model):
  
  """
  Stores a single trip data.
  
  There are three category of trip(short, mid and long range trip).
  
  It is related to the bookings and management through a ForeignKey relationship.
  
  It is related to transporters(drivers, mechanics and loaders through a many to many relationship.

  Admin also known as superuser can't be assign to a trip as management.
  """
  
  catgType = (
     ("sh", "Short Range"),
     ("md", "Mid Range"),
     ("lg", "Long Range")
  )
  
  statusType = (
     ("one", "Open"),
     ("two", "Close")
  )
  
  progressType = (
     ("1", "Departed"),
     ("2", "Pickup"),
     ("3", "Onroad"),
     ("4", "Delivered"),
     ("5", "Arrived")
  )
  
  sn = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name="id")
  booking = models.OnetoOneField(Booking, on_delete=models.CASCADE, related_name="trip")
  category = models.CharField(max_length=3, choices=catgType)
  driver = models.ManytoManyField(Driver, related_name='trips', limit_choices_to={'active': False})
  mechanic = models.ManytoManyField(Mechanic, related_name='trips', limit_choices_to={'active': False})
  loader = models.ManytoManyField(Loader, related_name='trips', limit_choices_to={'active': False})
  management = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='trips',
  limit_choices_to={'is_superuser': False})
  report = models.IntegerField(verbose_name='Expected report')
  status = models.CharField(max_length=3, choices=statusType)
  progress = models.CharField(max_length=2, choices=progressType)
  date = models.DateTimeField()
  
  
  def __str__(self):
    text = '%s(schedule: %s)' % (self.get_category_display(), self.date)
    return text.title()
  
  # overide the save method.
  def save(self, *args, **kwargs):
    if self.status == "one":
      flip(self.driver, True)
      flip(self.mechanic, True)
      flip(self.loader, True)
    else:
      flip(self.driver, False)
      flip(self.mechanic, False)
      flip(self.loader, False)
      
    if not self.management.is_superuser:
      super().save(*args, **kwargs) 
    else:
      text = "Admin can't be assign to a trip"
      raise ValidationError(text)
      
  
  


class Report(models.Model):
  
  """
  Stores a single report data.
  
  A report is related to the trip table through a foreign key relationship
  
  """
  
  statusType = (
     ('G', 'Green'),
     ('R', 'Red'),
     ('Y', 'Gray')
  )
  
  trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='reports')
  status = models.CharField(max_length=5, choices=statusType)
  remark = models.CharField(max_length=30)
  coord = models.CharField(max_length=200)
  date = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    text = '%s (%s)' % (self.get_status_display(), self.date)
    return text.title()
  
 
 
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
  trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='messages')
  label = models.CharField(max_length=2, choices=labelType)
  status = models.CharField(max_length=2, choices=statusType)
  date = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    text = '%s...(%s)' % (self.message[:10], self.get_status_display())
    return text.title()
    
