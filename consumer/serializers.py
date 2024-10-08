from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Fitting

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)
    
    class Meta:
        model = Profile
        fields = ['id','username','user','email','address', 'phone', 'golf_club_size']

class FittingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fitting
        fields = ['id','user','date', 'time', 'comments', 'status']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'profile']
