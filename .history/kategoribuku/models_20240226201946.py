from django.db import models

# Create your models here.
class Kategoribuku(models.Model):
    kategoriid = models.IntegerField(db_column='KategoriID', primary_key=True)  # Field name made lowercase.
    namakategori = models.CharField(db_column='NamaKategori', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'kategoribuku'