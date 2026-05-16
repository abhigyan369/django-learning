from django.db import models

# Create your models here.
class Project(models.Model):
    topic = models.CharField(max_length=100)
    language_used = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return self.topic
    
    