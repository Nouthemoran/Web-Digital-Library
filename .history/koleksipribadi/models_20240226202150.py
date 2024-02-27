from django.db import models
from buku.models import Buku
from user.models import User

# Create your models here.
class Koleksipribadi(models.Model):
    koleksiid = models.IntegerField(db_column='KoleksiID', primary_key=True)  # Field name made lowercase.
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='UserID')  # Field name made lowercase.
    bukuid = models.ForeignKey(Buku, models.DO_NOTHING, db_column='BukuID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'koleksipribadi'