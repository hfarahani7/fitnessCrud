from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class DateTimeManager(models.Manager):
    def getTime(self):
        return(self.strfTime("%m%d%Y"))
    def getDate(self):
        return(self.strfTime("%H%M%S"))

class TrainingSession(models.Model):
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=120)
    dateTime = models.DateTimeField()
    date = DateTimeManager.getDate(dateTime)
    time = DateTimeManager.getTime(dateTime)
    instructorID = models.ForeignKey(User, on_delete=models.CASCADE)
    maxParticipants = models.IntegerField()

# Create your models here.
