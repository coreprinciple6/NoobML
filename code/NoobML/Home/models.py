import ast
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
from django.db import models
from pytz import unicode


class User(AbstractUser):
    photo = models.ImageField(upload_to='Home/', blank=True, validators=[FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'])])

    def __str__(self):
        return f'''
                 username: {self.username}
                 email: {self.email}
                 first_name: {self.first_name}
                 last_name: {self.last_name}
   
          '''
#for list attribute in models
#class ListField(models.TextField):

    #def from_db_value(self, value, expression, connection, context):

  #  def __init__(self, *args, **kwargs):
 #       super(ListField, self).__init__(*args, **kwargs)

 #   def to_python(self, value):
  #      if not value:
   #         value = []
#
    #    if isinstance(value, list):
    #        return value

  #      return ast.literal_eval(str(value))

  #  def get_prep_value(self, value):
  #      if value is None:
  #          return value

  #      return unicode(value)

 #   def value_to_string(self, obj):
  #      value = self._get_val_from_obj(obj)
   #     return self.get_db_prep_value(value)


L_CHOICE = [('Supervised','Supervised'),('Unsupervised','Unsupervised')]
T_CHOICE = [('Classification','Classification'),('Regression','Regression')]
class Project(models.Model):
    U_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    Name = models.CharField(max_length=500)
    Train_csv = models.FileField(upload_to='Home/excel',blank=False, validators=[FileExtensionValidator(allowed_extensions=['csv'])])
    Test_csv = models.FileField(upload_to='Home/excel',blank=False, validators=[FileExtensionValidator(allowed_extensions=['csv'])])
    Learning = models.CharField(max_length=250,choices=L_CHOICE,default=1, blank=False)
    Type = models.CharField(max_length=250,choices=T_CHOICE, default=0, blank=False)
    Target = models.CharField(max_length=250)
    Input_Attributes = models.TextField(max_length=1000, blank=False)

    def __str__(self):
        return f'''
                 U_id: {self.U_id}
                 Name: {self.Name}
                 Train_csv: {self.Train_csv}
                 Test_csv: {self.Test_csv}
                 Learning: {self.Learning}
                 Type: {self.Type}
                 Target: {self.Target}
                 Input_Attributes: {self.Input_Attributes}

          '''

    class Meta:
        unique_together = (('Name', 'U_id'))

class Inference(models.Model):
    P_id = models.ForeignKey(Project, on_delete=models.CASCADE, blank=False)
    Model_Name = models.CharField(max_length=250)
    Score = models.FloatField()
    Features = models.TextField(max_length=1000, blank=False)

    def __str__(self):
        return f'''
                 P_id: {self.P_id}
                 Model_name: {self.Model_Name}
                 Score: {self.Score}
                 Features: {self.Features}
          '''