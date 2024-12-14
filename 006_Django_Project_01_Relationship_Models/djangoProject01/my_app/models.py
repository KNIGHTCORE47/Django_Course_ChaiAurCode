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
    

# NOTE - Here we have imported User class from django.contrib.auth.models which is a built-in class in Django
from django.contrib.auth.models import User

### NOTE - One to Many Relationship
class Product_Review(models.Model):
    product = models.ForeignKey(Different_Chais, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(default=0)
    comment = models.TextField(default='')
    date_field = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Review for {self.product.name} by {self.user.username}"
    

### NOTE - Many to Many Relationship
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    product_varieties = models.ManyToManyField(Different_Chais, related_name='stores')

    def __str__(self):
        return self.name



### NOTE - One to One Relationship
class Product_Certificate(models.Model):
    product = models.OneToOneField(Different_Chais, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateField(default=timezone.now)
    expiration_date = models.DateField()

    def __str__(self):
        return f"Certificate for {self.product.name}"