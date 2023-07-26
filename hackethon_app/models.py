from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Hackethon(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    background_image = models.ImageField(upload_to='static/')
    hackethon_image = models.ImageField(upload_to='static/')
    start_at = models.DateTimeField()
    ends_at = models.DateTimeField()
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " | " + str(self.username)



class HackethonRegistration(models.Model):
    hackethon_name = models.ForeignKey(Hackethon, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.username) + " | " + self.hackethon_name.title


class HackethonSubmission(models.Model):
    hackethon_name = models.ForeignKey(HackethonRegistration, on_delete=models.CASCADE)
    submission = models.FileField(upload_to='static/')

    def __str__(self):
        return str(self.hackethon_name.username) + " | " + self.hackethon_name.hackethon_name.title


