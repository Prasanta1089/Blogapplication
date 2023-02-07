from django.db import models

# Create your models here.

class Contact(models.Model):
    serialno = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=225)
    Phonenumber=models.CharField(max_length=15)
    Email=models.CharField(max_length=100)
    Content= models.TextField()
    timeStamp= models.DateField(auto_now_add=True, blank=True)
    
    
    def __str__(self):
        return  self.Name