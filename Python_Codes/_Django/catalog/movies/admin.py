from django.contrib import admin
from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_date', 'isPublished') # These parameters will be display on the admin panel of movies page.
    list_display_links = ('id', 'name') # These parameters will have the links.
    list_filter = ('created_date',)
    list_editable = ('isPublished',)
    search_fields = ('name', 'description')
    list_per_page = 10 # This will show 10 records per page.


    

# Register your models here.

admin.site.register(Movie, MovieAdmin) # this is the model we created in the models.py file