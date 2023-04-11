from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    capabilities_needed = models.CharField(max_length=100)
    disease_area = models.CharField(max_length=100)
    study_type = models.CharField(max_length=100)
    submitted_by = models.CharField(max_length=100)
