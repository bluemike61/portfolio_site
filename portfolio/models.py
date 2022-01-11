from django.db import models

# Create your models here.

class Project(models.Model):
    #create class and inherit from model class
    title = models.CharField(max_length=50)
    #creates a title for project, and how long it should be
    description = models.CharField(max_length=200)
    #creates a description for project, and how long it should be
    image = models.ImageField(upload_to='portfolio/images/')
    #image to display as a thumbnail
    url = models.URLField(blank=True)
    #specific url
    
    def __str__(self):
        return self.title