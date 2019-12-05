from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from vehicles.models import Vehicle


class Post(models.Model):
    CATEGORY_CHOICES = [
        (1,'Specs'),
        (2,'Mechanical'),
        (3,'Interior'),
        (4,'Exterior'),
        (5,'Miscellaneous'),
    ]
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100, default=None, blank=True, null=True,)
    content = models.TextField()
    description = models.CharField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.IntegerField(choices=CATEGORY_CHOICES, blank=True, null=True,)
    tags = models.CharField(max_length=500, default=None, blank=True, null=True,)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    context = models.ForeignKey(Vehicle, default=None, blank=True, null=True, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-date_posted']
        
    def __str__(self):
        return self.title


class ServiceManual(models.Model):
    display_filename = models.CharField(max_length=100)
    fsm_file = models.FileField(upload_to='service_manuals')
    date_uploaded = models.DateTimeField(default=timezone.now)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    uploader = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.display_filename