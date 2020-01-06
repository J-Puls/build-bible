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
    title = models.CharField(max_length=60)
    subtitle = models.CharField(max_length=30, default=None, blank=True, null=True,)
    content = models.TextField()
    description = models.CharField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    category = models.IntegerField(choices=CATEGORY_CHOICES, blank=True, null=True,)
    tags = models.CharField(max_length=100, default=None, blank=True, null=True,)
    times_viewed = models.IntegerField(default=0)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="posts")
    last_modified_by = models.ForeignKey(User, null=True, related_name='entry_modifiers', blank=True, on_delete=models.SET_NULL)
    last_modified = models.DateTimeField(auto_now_add=True)
    context = models.ForeignKey(Vehicle, default=None, blank=True, null=True, on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['-date_posted']
        
    def __str__(self):
        return f'Title: {self.title}\nDate Posted: {self.date_posted}\nViews: {self.times_viewed}'


class ServiceManual(models.Model):
    display_filename = models.CharField(max_length=100)
    fsm_file = models.FileField(upload_to='service_manuals')
    date_uploaded = models.DateTimeField(default=timezone.now)
    times_downloaded = models.IntegerField(default=0)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    uploader = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.display_filename