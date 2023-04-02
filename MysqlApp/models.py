from django.db import models

# Create your models here.
class RegisterForm(models.Model):
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Event_Name = models.CharField(max_length=100)
    Contact_Number = models.CharField(max_length=50)
    Email_ID = models.EmailField()

    class Meta:
        db_table = 'regdata'
    


