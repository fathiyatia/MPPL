from django.db import models
from datetime import date
from django.utils import timezone

# Create your models here.

class Documents(models.Model):
    CATEGORY = (
       ('Surat Masuk', 'Surat Masuk'),
       ('Surat Keluar', 'Surat Keluar'), 
    )
    
    tanggal_terima = models.DateField(default=date.today, null=True)
    dari_atau_ke = models.CharField(max_length=500, null=True)
    no_surat = models.CharField(max_length=200, null=True)
    tanggal_surat = models.DateField(default=date.today, null=True)
    hari_jam = models.DateTimeField(default=timezone.now, null=True)
    tempat = models.CharField(max_length=500, null=True)
    acara = models.TextField(null=True)
    keterangan = models.TextField(null=True)
    date_input = models.DateTimeField(auto_now_add=True, null=True)
    kategori = models.CharField(max_length=200, null=True, choices=CATEGORY)
    uploaded_file = models.FileField(null=True)

    timestamp_lastupdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.acara