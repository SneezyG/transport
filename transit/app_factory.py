import factory
from factory import fuzzy
from faker import Faker
from datetime import datetime
from app.models import User
import uuid





class TransporterFactory(factory.django.DjangoModelFactory):

  class Meta: 
      model = 'app.Transporter'
      django_get_or_create = ('sn',)
      
  sn = factory.Faker("ean8")
  firstName = factory.Faker('first_name')
  lastName = factory.Faker('last_name')
  birthday = factory.Faker('date_between', start_date=datetime(1980, 1, 1), end_date=datetime(1990, 1, 1))
  sex = fuzzy.FuzzyChoice(choices=['M', 'F', 'P'])
  phone = factory.Faker('phone_number')
  aptNo = factory.Faker('random_int', min=1, max=30)
  laneNo = factory.Faker('random_int', min=1, max=10)
  street = factory.Faker('street_name')
  city = factory.Faker('city')
  state = factory.Faker('state')
  nationality = factory.Faker('country')
  zipcode = factory.Faker('postcode')
  
  
  
  
  
class BookingFactory(factory.django.DjangoModelFactory):

  class Meta: 
      model = 'app.Booking'
      django_get_or_create = ('sn',)
      
  sn = factory.LazyFunction(lambda: str(uuid.uuid4()))
  name = factory.Faker("company")
  booker = factory.Faker("name")
  name1 = factory.Faker("name")
  name2 = factory.Faker("name")
  contact1 = factory.Faker("phone_number")
  contact2 = factory.Faker("phone_number")
  contact3 = factory.Faker("phone_number")
  charges = factory.Faker("random_number", digits=5, fix_len=True)
  paid = factory.Faker("boolean")
  goods = factory.Faker("sentence")
  pickup = factory.Faker("address")
  delivery = factory.Faker("address")
  
  
  
  
  
class TripFactory(factory.django.DjangoModelFactory):

  class Meta: 
      model = 'app.Trip'
      django_get_or_create = ('sn',)
      
  sn = factory.LazyFunction(lambda: str(uuid.uuid4()))
  booking = factory.SubFactory(BookingFactory)
  category = fuzzy.FuzzyChoice(choices=['sh', 'md', 'lg'])
  management = factory.Iterator(User.objects.filter(user_type="supervisor"))
  report = factory.Faker('random_int', min=3, max=7)
  status = "one"
  progress = "0"
  created_date = factory.Faker('date_between', start_date=datetime(2024, 1, 20), end_date=datetime(2024, 2, 20))
  due_date = factory.Faker('date_between', start_date=datetime(2024, 3, 20), end_date=datetime(2024, 4, 20))
  
  
  @factory.post_generation
  def transporters(self, create, extracted, **kwargs):
      if not create or not extracted:
          return
      self.transporters.add(*extracted)
      
      
      