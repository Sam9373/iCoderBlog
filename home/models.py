from django.db import models

# Create your models here.
class Contact(models.Model):
    Sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    phone=models.CharField(max_length=13)
    content=models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)
    
# It will  give the object name as name field for admin contact object  
    def __str__(self):
        return self.name