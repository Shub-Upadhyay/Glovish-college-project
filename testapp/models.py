from django.db import models

# Create your models here.
class Login(models.Model):
    username = models.EmailField(max_length=50)
    password = models.CharField(max_length=30)


class Trying(models.Model):
    Choice = (
   ('B & W', 'Black & White'),
   ('Colour', 'Colour')
   )
    username = models.EmailField(default=None)
    usn = models.CharField(max_length=20 , default=None)
    print = models.BooleanField(default=False )
    bindings = models.BooleanField(default=False)
    print_type= models.CharField(choices=Choice, max_length=128 , default=None)
    file = models.FileField(default=None)
    total_pages = models.IntegerField(default=None)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    print_status = models.TextField(default=False)
    amount = models.IntegerField(default=None)
    payment = models.BooleanField(default=False)