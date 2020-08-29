from django.db.models.signals import pre_save,post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save,sender = User)
def Create_Profile(sender,instance,create,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender = User)
def Create_Profile(sender,instance,**kwargs):
    instance.profile.save()