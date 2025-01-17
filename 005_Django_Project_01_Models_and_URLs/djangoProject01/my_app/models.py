from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICES = [
        ('BLT', 'Black Tea'),
        ('MLT', 'Milk Tea'),
        ('GLT', 'Green Tea'),
        ('GNT', 'Ginger Tea'),
        ('MNT', 'Mint Tea'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3, choices=CHAI_TYPE_CHOICES, default='BLT')
    description = models.TextField(max_length=255, default='')
    price = models.DecimalField(max_digits=10, default=0.00, decimal_places=2)

    def __str__(self):
        return self.name
