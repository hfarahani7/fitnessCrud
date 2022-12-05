from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Session, GroupClass, TrainerData, TraineeData

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TrainerDataSerializer(serializers.Serializer):
    age = serializers.IntegerField(read_only=False)
    id = serializers.IntegerField(source='id')
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