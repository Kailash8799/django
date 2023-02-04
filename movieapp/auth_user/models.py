from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=20)
    user_email = models.EmailField(max_length=50)
    user_password = models.CharField(max_length=254)
    
    def __str__(self):
        return self.user_name
    
class Contact(models.Model):
    message_id = models.AutoField(primary_key=True)
    m_u_name = models.CharField(max_length=20)
    m_email = models.CharField(max_length=30)
    u_message = models.TextField()

    def __str__(self):
        return self.m_u_name