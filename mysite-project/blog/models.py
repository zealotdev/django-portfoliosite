from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=40)
    #pup_date = models.DateTimeField(timezone.add)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __tr__(self):
        return self.title
