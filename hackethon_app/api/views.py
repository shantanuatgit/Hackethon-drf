from django.shortcuts import render

from ..models import *
from .serializers import *
from .permissions import *

from rest_framework import generics
from rest_framework.validators import ValidationError
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class HackethonList(generics.ListAPIView, generics.GenericAPIView):
    """Listing Hackethon objects"""
    queryset = Hackethon.objects.all()
    serializer_class = HackethonSerializer


class HackethonCreate(generics.CreateAPIView):
    """Host a new Hackethon"""
    queryset = Hackethon.objects.all()
    serializer_class = HackethonSerializerForCreate
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
       serializer.save(username=self.request.user)


class HackethonRegistrationList(generics.ListAPIView, generics.GenericAPIView):
    """Listing the Hackethon registered by specific user"""
    serializer_class = HackethonRegistrationSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminOnly]

    def get_queryset(self):
        return HackethonRegistration.objects.filter(username=self.request.user)
    
    
class HackethonRegistrationCreate(generics.CreateAPIView):
    """Registering in a Hackethon"""
    serializer_class = HackethonRegistrationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
       return HackethonRegistration.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        hackethon = Hackethon.objects.get(pk=pk)
        username = self.request.user
        registered_queryset = HackethonRegistration.objects.filter(hackethon_name=hackethon, username=username)
        if registered_queryset.exists():
            raise ValidationError("You have already registered for this Hackethon.")
        
        serializer.save(hackethon_name=hackethon, username=username)

        
class HackethonSubmissionList(generics.ListAPIView, generics.GenericAPIView):
    """Listing the submissions for a registered Hackethon"""
    serializer_class = HackethonSubmissionSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrAdminOnly]

    def get_queryset(self):
        return HackethonSubmission.objects.filter(hackethon_name__username=self.request.user)


class HackethonSubmissionCreate(generics.CreateAPIView):
    """Submitting solution for registered hackethon"""
    serializer_class = HackethonSubmissionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HackethonSubmission.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        try:
            registered_hackethon = HackethonRegistration.objects.get(pk=pk)
        except:
            raise ValidationError("you are not registered to this Hackethon.")

        
        submitted_queryset = HackethonSubmission.objects.filter(hackethon_name=registered_hackethon)
        if submitted_queryset.exists():
            raise ValidationError("you have already submitted.")
        
        serializer.save(hackethon_name=registered_hackethon)
    


    