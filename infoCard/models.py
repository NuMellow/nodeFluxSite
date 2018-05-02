from django.db import models

class Card(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
   # thumbnail = models.ImageField(upload_to=None, height_field=None


    def __str__(self):
        return self.title
