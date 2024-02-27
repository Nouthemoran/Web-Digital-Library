from django.db import models
from kategoribuku import 

# Create your models here.
class Buku(models.Model):
    bukuid = models.IntegerField(db_column='BukuID', primary_key=True)  # Field name made lowercase.
    judul = models.CharField(db_column='Judul', max_length=255)  # Field name made lowercase.
    kategoriid = models.ForeignKey(Kategoribuku, models.DO_NOTHING, db_column='KategoriID')
    penulis = models.CharField(db_column='Penulis', max_length=255)  # Field name made lowercase.
    penerbit = models.CharField(db_column='Penerbit', max_length=255)  # Field name made lowercase.
    tahunterbit = models.IntegerField(db_column='TahunTerbit')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'buku'