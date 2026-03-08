from django.db import models

# Create your models here.
class CsvUpload(models.Model):
    csv_file = models.FileField(upload_to='uploads/', null=True, blank=True)