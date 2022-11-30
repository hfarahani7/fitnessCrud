from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class TrainerData(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    age = models.PositiveIntegerField(null=True)
    gender = models.CharField(
        choices = [
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Other', 'Other')
        ],
        default='Male',
        max_length=10
    )
    bio = models.CharField(max_length=120)

class TraineeData(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    weight = models.PositiveIntegerField()
    height = models.PositiveIntegerField()

class GroupClass(models.Model):
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=120, null=True)
    dateTime = models.DateTimeField(null=True)
    # date = DateTimeManager.getDate(dateTime)
    # time = DateTimeManager.getTime(dateTime)
    trainerID = models.ForeignKey(TrainerData, on_delete=models.CASCADE, null=True)
    maxParticipants = models.IntegerField(null=True)

    def __str__(self):
        return self.title

    def isFull(self):
        return(self.maxParticipants < len(self.participants))

class Session(models.Model):
    traineeID = models.ManyToManyField(TraineeData)
    classID = models.ForeignKey(GroupClass, on_delete=models.DO_NOTHING)
    