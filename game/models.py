from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Game(models.Model):
    name=models.CharField(max_length=250)
    header_image= models.ImageField(null=True,blank=True, upload_to ="images/")
    title_tag=models.CharField(max_length=250, default="welcome to my site")
    made_by=models.CharField(max_length=250)
    description=models.TextField()
    year_of_release=models.DateField()
    price=models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name + '-' + str(self.price)+'BD'
    
    def get_absolute_url(self):
        return reverse('home')