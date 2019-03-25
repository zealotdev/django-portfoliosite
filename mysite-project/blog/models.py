from django.db import models
from taggit.manager import TaggableManager


tags = (
    ('Programming', Programming),
    ('Hacking', Hacking),
    ('Technology', Technology),
    ('Lifestyle', Lifestyle),
)

class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=20)
    text = models.TextField()
    pub_date= models.DateTimeField()
    tag = TaggableManager(choices = 'tags')
