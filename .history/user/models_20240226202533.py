from django.db import models
from buku.models import Buku
from user.models import User

# Create your models here.
class Ulasanbuku(models.Model):
    ulasanid = models.IntegerField(db_column='UlasanID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    bukuid = models.ForeignKey(Buku, models.DO_NOTHING, db_column='BukuID')  # Field name made lowercase.
    ulasan = models.TextField(db_column='Ulasan')  # Field name made lowercase.
    rating = models.IntegerField(db_column='Rating')  # Field name made lowercase.