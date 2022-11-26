from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# class Trainer(User):
#     firstName = models.TextField()
#     lastName = models.TextField()
#     bio = models.TextFiel(max_length=120)
#     age = models.PositiveIntegerField()

#     def __str__(self):
#         return (self.firstName + " " + self.lastName)

# class Trainee(models.User):
#     firstName = models.TextField()
#     lastName = models.TextField()
#     age = models.PositiveIntegerField()
#     weight = models.PositiveIntegerField()
#     heightInches = models.PositiveIntegerField()

#     def __str__(self):
#         return (self.firstName + " " + self.lastName)

# class DateTimeManager(models.Manager):
#     def getTime(self):
#         return(self.strfTime("%m%d%Y"))
#     def getDate(self):
#         return(self.strfTime("%H%M%S"))

class GroupClass(models.Model):
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=120, null=True)
    dateTime = models.DateTimeField(null=True)
    # date = DateTimeManager.getDate(dateTime)
    # time = DateTimeManager.getTime(dateTime)
    instructorID = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    maxParticipants = models.IntegerField(null=True)
    participants = models.JSONField(null=True) 

    def __str__(self):
        return self.title

    def isFull(self):
        return(self.maxParticipants < len(self.participants))

class Session(models.Model):
    # trainerID = models.ForeignKey(Trainer)
    # traineeID = models.ForeignKey(Trainee)
    classID = models.ForeignKey(GroupClass, on_delete=models.DO_NOTHING)