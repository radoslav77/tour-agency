from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="autor")
    date = models.DateField(auto_now=True)
    text = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    from_date = models.DateField(auto_now=False)
    to_date = models.DateField(auto_now=False)
    image = models.URLField(max_length=300, blank = True)  




class Country(models.Model):
    holiday = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="holiday")
    country = models.CharField(max_length=150)
    categories = models.CharField(max_length=100)
    
    class Meta:        
        ordering = ['country']
    
    def __str__(self):
        return f"{self.country}"

    

class Archive(models.Model):
    archive = models.BooleanField(default=False)
    title = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="title_arch")
    date = models.DateField(auto_now=False)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.date}"

class Search(models.Model):
    Choose_country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="where")
    When_would_you_travel = models.DateField(auto_now=False)
    How_many_people = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return f"{self.country},{self.travel},{self.people}"

class Booking(models.Model):
    holiday = models.CharField(max_length=200)
    from_date = models.DateField(auto_now=False)
    till_date = models.DateField(auto_now=False)
    travelers = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])

    def __str__(self):
        return f"{self.holiday},{self.from_date}, {self.travelers}"

class Checkout(models.Model):
    title = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyer")
    user_name = models.CharField(max_length=300)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=60)
    card_name = models.CharField(max_length=150)
    card_number = models.IntegerField()
    expmonth = models.CharField(max_length=50)
    expyear = models.IntegerField()
    cvv = models.IntegerField()
    post_code = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.title}"