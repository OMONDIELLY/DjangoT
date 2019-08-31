from django.db import models
from django.urls import reverse
# Create your models here.
class product(models.Model):
       title    =   models.CharField(max_length=20)
       description = models.TextField(blank=True , null=True)
       price =       models.DecimalField(decimal_places=2, max_digits=65 ) 
       summary =   models.TextField()
  

       def get_absolute_url(self):
           return reverse("products:product-detail",kwargs={})
       #     return f"/products/{self.id}/"
     