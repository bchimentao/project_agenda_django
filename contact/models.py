from django.db import models
from django.utils import timezone

# after any changes here:
# python manage.py makemigrations  --> create the files for migration
# python manage.py migrate         --> migrate

#id (primary key - automatic)



class Contact(models.Model):
    first_name = models.CharField(max_length=50) #Charfield is for strings
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True) #blank=True allows optional filling
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'