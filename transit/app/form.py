
from django.forms import ModelForm
from django.core.exceptions import ValidationError



class TripAdminForm(ModelForm):
  
  """
  ensure that a superuser is not added to a Trip through the management relationship.
  
  """
  
  def clean_management(self):
     data = self.cleaned_data["management"]
     if data.is_superuser:
       text= "Admin(superuser) can't be assign to a trip"
       raise ValidationError(text)
     else:
      return data
 