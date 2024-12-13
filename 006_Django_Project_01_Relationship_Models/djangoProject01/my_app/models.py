from django.db import models
from django.utils import timezone

# Create your models here.
class Different_Chais(models.Model):
    CHAI_TYPE_CHOICES = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('KL', 'KIWI'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI'),
    ]

    name = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='uploads/', default='')
    current_time = models.DateTimeField(default=timezone.now)
    chai_type = models.CharField(max_length=2,
    choices=CHAI_TYPE_CHOICES, default='ML')
    description = models.TextField(max_length=255, default='')
    price = models.DecimalField(max_digits=10, default=0.00, decimal_places=2)


    def __str__(self):
        return self.name
