from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Session, GroupClass, TrainerData, TraineeData

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user
    
    class Meta:
        model = User
        fields = ( "id", "username", "password", )

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TrainerDataSerializer(serializers.Serializer):
    age = serializers.IntegerField(read_only=False)
    gender = serializers.CharField(read_only=False)
    bio = serializers.CharField(read_only=False)

    class Meta:
        model = TrainerData
        fields = ('id', 'age', 'gender', 'bio')

    def create(self, validated_data):
        return TrainerData.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.age = validated_data.get('age', instance.age)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.bio = validated_data.get('bio', instance.bio)

        return instance

class TraineeDataSerializer(serializers.Serializer):
    weight = serializers.IntegerField(read_only=False)
    height = serializers.IntegerField(read_only=False)

    class Meta:
        model = TraineeData
        fields = ('id', 'weight', 'height')
    
    def create(self, validated_data):
        return TraineeData.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.height = validated_data.get('height', instance.height)

class GroupClassSerializer(serializers.Serializer):
    title = serializers.CharField(read_only=False)
    description = serializers.CharField(read_only=False)
    dateTime = serializers.DateTimeField(read_only=False)
    maxParticipants = serializers.IntegerField(read_only=False)

    class Meta:
        model = GroupClass

    def create(self, validated_data):
        return GroupClass.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.dateTime = validated_data.get('dateTime', instance.dateTime)
        instance.trainerID = validated_data.get('trainerID', instance.trainerID)
        instance.maxParticipants = validated_data.get('maxParticipants', instance.maxParticipants)

class SessionSerializer(serializers.Serializer):
    traineeID = serializers.IntegerField(read_only=False)
    classID = serializers.IntegerField(read_only=False)

    class Meta:
        model = Session

    def create(self, validated_data):
        return Session.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.traineeID = validated_data.get('traineeID', instance.traineeID)
        instance.classID = validated_data.get('classID', instance.classID)