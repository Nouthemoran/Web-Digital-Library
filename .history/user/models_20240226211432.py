from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    userid = models.AutoField(db_column='UserID', primary_key=True)  # Field name made lowercase.
    namalengkap = models.CharField(db_column='NamaLengkap', max_length=255)  # Field name made lowercase.
    alamat = models.TextField(db_column='Alamat')  # Field name made lowercase.
    
    def __str__(self):
            return self.username