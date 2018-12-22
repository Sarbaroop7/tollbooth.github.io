from django.db import models

class User(models.Model):
    Title = models.CharField(max_length = 4)
    Name = models.CharField(max_length = 80)
    DOB = models.DateTimeField()
    Address = models.TextField(max_length = 500)
    City = models.CharField(max_length = 50)
    State = models.CharField(max_length = 50)
    Nationality = models.CharField(max_length = 60)
    Car_plate_number = models.CharField(max_length = 80)
    timestamp = models.DateTimeField()
    


    
