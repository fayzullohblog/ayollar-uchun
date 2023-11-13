from django.db import models


from utils.models import BaseModel

# Create your models here.
class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images')
    phone = models.CharField(max_length=255)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Advertisement'
        verbose_name_plural = 'Advertisements'
        
class UsersRule(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        verbose_name = 'Users Rule'
        verbose_name_plural = 'Users Rules'
    
class Connect(models.Model):
    phone = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    email = models.EmailField(unique=True, blank=True)
    address  = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.phone)
    
    class Meta:
        verbose_name = 'Connect'
        verbose_name_plural = 'Connects'
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, blank=True)
    phone = models.CharField(max_length=255)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
