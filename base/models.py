from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=50)
    subject= models.CharField(max_length=50)
    message = models.TextField()
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.name

