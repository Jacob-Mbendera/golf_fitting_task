from rest_framework import serializers
from .models import GettingStartedInfo

class GettingStartedInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GettingStartedInfo
        fields = ['content']