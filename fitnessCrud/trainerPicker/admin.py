from django.contrib import admin
from .models import GroupClass, Session, TraineeData, TrainerData

admin.site.register(GroupClass)
admin.site.register(Session)
admin.site.register(TraineeData)
admin.site.register(TrainerData)
# Register your models here.
