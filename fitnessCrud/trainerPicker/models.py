from django.db import models
from datetime import datetime
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser
from django.contrib.auth.base_user import AbstractBaseUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

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

    def __str__(self):
        return(self.id.username)

class TraineeData(models.Model):
    id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    weight = models.PositiveIntegerField()
    height = models.PositiveIntegerField()

    def __str__(self):
        return(self.id.username)

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

    def __str__(self):
        return(str(self.classID))


class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )
        user.save(using=self._db)

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True,
    )
    firstName = models.CharField(max_length = 20)
    lastName = models.CharField(max_length = 30)
    
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName', 'lastName']

    def __str__(self):
        return(self.firstName + " " + self.lastName)
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)