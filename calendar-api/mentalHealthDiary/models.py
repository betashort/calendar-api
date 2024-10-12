from django.db import models

# Create your models here.
class MentalHealthDirary(models.Model):
    
    class Meta:
        db_table = "MetalHealthDirary"
        
    id = models.CharField(verbose_name="id", primary_key=True, max_length=50, editable=False)
    
    title = models.CharField(verbose_name="title", max_length=50)
    
    description = models.CharField(verbose_name="description", max_length=500)
    
    start = models.CharField(verbose_name="start event date", max_length=50)