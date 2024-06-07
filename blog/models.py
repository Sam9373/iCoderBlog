from django.db import models

# Create your models here.
class Post(models.Model):
    Sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    content=models.TextField()
    author=models.CharField(max_length=13)
    slug=models.CharField(max_length=130)
    timeStamp=models.DateTimeField(blank=True)
    
# It will  give the object name as name field for admin contact object  
    def __str__(self):
        return self.title
