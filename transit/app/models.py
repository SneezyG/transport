
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
import uuid
import decimal



def driv(instance, filename):
  #create a unique path for drivers photo.
  return 'driver/driv_{0}/{1}'.format(instance.sn, filename)

def doc1(instance, filename):
  #create a unique path for doc1.
  return 'doc1/doc_{0}/{1}'.format(instance.sn, filename)
  
def doc2(instance, filename):
  #create a unique path for doc2.
  return 'doc2/doc_{0}/{1}'.format(instance.sn, filename)
  
    



class User(AbstractUser): 
  
  """
  store a single user data.
  extend the django abstract-user class.
  and this model is the new auth_user_model
  """
  
  office_line = models.CharField(max_length=15, verbose_name="Office-line", null=True, blank=True)
  personal_line = models.CharField(max_length=15, verbose_name="Personal-line", null=True, blank=True)
  is_agent = models.BooleanField(default=False, help_text="Designates that this user have access to the trip reporting part of this web-app", verbose_name="is-agent")
  
 
 
  
class Transporter(models.Model):
  
  """
  Transporters are freelancers which are paid based on the type and amount of trip they go.
  """
  
  sexType = (
      ('M', 'male'),
      ('F', 'female'),
      ('P', 'private'),
    )
    
  
  sn = models.CharField(max_length=30, unique=True, verbose_name='id')
  firstName = models.CharField(max_length=20, verbose_name='first name')
  lastName = models.CharField(max_length=20, verbose_name='last name')
  birthday = models.DateField()
  sex = models.CharField(max_length=1, choices=sexType)
  phone = models.CharField(max_length=15, verbose_name="phone number")
  aptNo = models.IntegerField(verbose_name='apartment number')
  laneNo = models.IntegerField(verbose_name='lane number')
  street = models.CharField(max_length=30)
  city = models.CharField(max_length=30)
  state = models.CharField(max_length=30,)
  nationality = models.CharField(max_length=30)
  zipcode = models.IntegerField()
  photo = models.ImageField(upload_to=driv, null=True, blank=True)
  date = models.DateTimeField(auto_now_add=True)
  

  def fullName(self):
    "Returns the person's full name."
    verbose_name='full name'
    fullname = '%s %s' % (self.firstName, self.lastName)
    return fullname.upper()
    
    
  def __str__(self):
    text = '%s %s' % (self.firstName, self.lastName)
    return text.title()
    
 
  def address(self):
    "Return the address of the person."
    address = 'no %s, lane %s, %s, %s, %s' % (self.aptNo, self.laneNo, self.street, self.city, self.state)
    return address.title()





class Payroll(models.Model):
  
 """
  This is rather a simple model to persist the amount paid per trip to freelancer transporters.
  
  The amount pay per trip depend on the amount & type of trip.
 """
  
 short_range = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="pay/short-range trip in $")
 mid_range = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="pay/mid-range trip in $")
 long_range = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="pay/long-range trip in $")
 date = models.DateTimeField(auto_now=True)
 
 



class Booking(models.Model):
  
  """
  Stores a single trip-booking data.
  
  This model also includes two file fields to store important bookings documents.
  """
  
  sn = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name="id")
  name = models.CharField(max_length=40, verbose_name="Company's name", null=True, blank=True)
  booker = models.CharField(max_length=40, verbose_name="Booker's name")
  name1 = models.CharField(max_length=40, verbose_name="Pick-up name")
  name2 = models.CharField(max_length=40, verbose_name="Delivery name")
  contact1 = models.CharField(max_length=15, verbose_name="Booker's contact")
  contact2 = models.CharField(max_length=15, verbose_name="Pick-up contact")
  contact3 = models.CharField(max_length=15, verbose_name="Delivery contact")
  charges = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Amount due($)")
  paid = models.BooleanField(default=False)
  goods = models.TextField(verbose_name="Goods description")
  pickup = models.CharField(max_length=150, verbose_name="pickup address")
  delivery = models.CharField(max_length=150, verbose_name="delivery address")
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
  
  It is related to the Booking and Management through a ForeignKey relationship.
  
  It is related to transporters(drivers, mechanics and loaders) through a many to many relationship.

  Supervisor also known as superuser can't be assign to a trip as management.
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
     ("0", "pending"),
     ("1", "Departed"),
     ("2", "Pickup"),
     ("3", "Onroad"),
     ("4", "Delivered"),
     ("5", "Arrived")
  )
  
  sn = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name="id")
  booking = models.OneToOneField(Booking, on_delete=models.CASCADE, related_name="trip")
  category = models.CharField(max_length=3, choices=catgType)
  transporters = models.ManyToManyField(Transporter, related_name='trips')
  management = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='trips',
  limit_choices_to={'is_superuser': False, 'is_agent': False})
  report = models.IntegerField(verbose_name='Expected report')
  status = models.CharField(max_length=3, choices=statusType, default="one")
  progress = models.CharField(max_length=2, choices=progressType, default="0")
  date = models.DateTimeField()
  
  
  def __str__(self):
    text = '%s(schedule: %s)' % (self.get_category_display(), self.date)
    return text.title()
      
  
  


class Report(models.Model):
  
  """
  Stores a single report data.
  
  A report is related to the trip table through a foreign key relationship.
  """
  
  statusType = (
     ('G', 'Green'),
     ('R', 'Red'),
     ('Y', 'yellow')
  )
  
  progressType = (
     ("0", "pending"),
     ("1", "Departed"),
     ("2", "Pickup"),
     ("3", "Onroad"),
     ("4", "Delivered"),
     ("5", "Arrived")
  )
  
  trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='reports')
  status = models.CharField(max_length=2, choices=statusType)
  progress = models.CharField(max_length=2, choices=progressType, default="0")
  remark = models.CharField(max_length=25)
  longitude = models.DecimalField(max_digits=9, decimal_places=6)
  latitude = models.DecimalField(max_digits=8, decimal_places=6)
  date = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    text = '%s (%s)' % (self.get_status_display(), self.date)
    return text.title()
  
 
