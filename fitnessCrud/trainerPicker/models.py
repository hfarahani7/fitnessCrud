from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# class DateTimeManager(models.Manager):
#     def getTime(self):
#         return(self.strfTime("%m%d%Y"))
#     def getDate(self):
#         return(self.strfTime("%H%M%S"))

class TrainingSession(models.Model):
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=120, null=True)
    dateTime = models.DateTimeField(null=True)
    # date = DateTimeManager.getDate(dateTime)
    # time = DateTimeManager.getTime(dateTime)
    instructorID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    maxParticipants = models.IntegerField(null=True)
    participants = 

    def __str__(self):
        return self.title

    def isFull(self):
        return(self.maxParticipants < len(self.participants))

# Create your models here.
