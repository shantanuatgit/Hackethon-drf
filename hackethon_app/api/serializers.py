from rest_framework import serializers

from ..models import *


class HackethonSerializer(serializers.ModelSerializer):
    """Serializes hackethon object"""
    username = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Hackethon
        fields = ['title', 'description', 'background_image', 'hackethon_image', 'start_at', 'ends_at', 'username']


class HackethonSerializerForCreate(serializers.ModelSerializer):
    """Serializes hackethon object host hackethon"""
    class Meta:
        model = Hackethon
        exclude = ('username',)



class HackethonRegistrationSerializer(serializers.ModelSerializer):
    """Serializes Registration object"""
    username = serializers.StringRelatedField(read_only=True)
    hackethon_name = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = HackethonRegistration
        fields = '__all__'
        # exclude = ('hackethon_name',)


class HackethonSubmissionSerializer(serializers.ModelSerializer):
    """Serializes Submission object"""
    hackethon_name = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = HackethonSubmission
        fields = '__all__'