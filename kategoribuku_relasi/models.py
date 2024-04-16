from django.db import models
from buku.models import Buku
from kategoribuku.models import Kategoribuku

# Create your models here.
class Kategoribuku_relasi(models.Model):
    kategoribukuid = models.IntegerField(db_column='KategoriBukuID', primary_key=True)  # Field name made lowercase.
    kategoriid = models.ForeignKey(Kategoribuku, models.DO_NOTHING, db_column='KategoriID')  # Field name made lowercase.
    bukuid = models.ForeignKey(Buku, models.DO_NOTHING, db_column='BukuID')  # Field name made lowercase.

