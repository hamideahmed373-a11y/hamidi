from django.db import models
from django.contrib.auth.models import User
import cloudinary


class Base(models.Model):
    SHOP_TYPES = [
        ('service provider', 'service Provider'),
        ('seller', 'Seller'),
        ('agency', 'Agency'),
        ('consultant', 'Consultant'),
        ('freelancer', 'Freelancer'),
    ]

    phone=models.CharField(max_length=10)
    email=models.EmailField()
    place=models.CharField()
    name = models.CharField(max_length=200)
    description = models.TextField()
    shop_type = models.CharField(max_length=20, choices=SHOP_TYPES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    icon=models.ImageField(upload_to='uploads/shops')
    def __str__(self):
        return self.name

class Offers(models.Model):
    CATEGORIES = [
        ('Physical Product', 'Physical Product'),
        ('Digital Product', 'Digital Product'),
        ('service', 'Service'),
        ('subscription', 'Subscription'),
    ]

    shop = models.ForeignKey(Base, on_delete=models.CASCADE, related_name='shops')
    image=models.ImageField(upload_to='uploads/offers')
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class How(models.Model):
    video=models.FileField(upload_to='upload/how' )
