from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name='Movie Name')
    description = models.TextField(verbose_name='Movie Description')
    image = models.CharField(max_length=50, verbose_name='Image URL')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Created Date") # auto_now_add=True means that the field will be automatically set to now when the object is first created.
    isPublished = models.BooleanField(default=True, verbose_name='Is Published?')

    def __str__(self):
        return f"{self.name}" # this is what will be displayed in the admin panel
    
    def get_image_path(self):
        return '/img/' + self.image