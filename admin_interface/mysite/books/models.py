from django.db import models

# Create your models here.
class Books(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField(blank=True, null=True) # blank and null = true karke restriction hata rhe
    # publication_date ko empty bhi chhod sakte hai
    def __str__(self):
        return self.title
