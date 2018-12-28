from django.db import models
from django.utils import timezone

class Post(models.Model):
    """
    A single Blog post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="img", blank=True, null=True)
    

class Entry(models.Model):
    comment = models.CharField(max_length=500)
    user = models.CharField(max_length=200)
    body = models.TextField(max_length=500, null=True, default=None)
    date_posted = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return 'Entry #{}'.format(self.id)
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'entries'   
