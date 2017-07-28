from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.core.exceptions import ValidationError
from django.core.files.images import get_image_dimensions
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user= models.OneToOneField(User)
    bio=models.TextField(blank=True,null=True)
    image = models.FileField(upload_to='media/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

# class Profile(models.Model):
#     def generate_user_folder_image(instance, filename):
#         return "uploads/users/%s/%s.png" % (instance.user, 'avatar')
#     user = models.OneToOneField(User)
#     image= models.ImageField(upload_to=generate_user_folder_image)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)
#     post_save.connect(create_user_profile, sender=User)
