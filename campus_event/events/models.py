from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def __str__(self):
        return self.title


class Registration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    roll_number = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
   
    def __str__(self):
        return self.name
    
class Feedback(models.Model):
     user = models.ForeignKey(User, on_delete=models.CASCADE)
     rating = models.IntegerField()

def __str__(self):
        return f"{self.user.username} - {self.rating}⭐"