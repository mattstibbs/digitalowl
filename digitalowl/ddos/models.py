from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver


class DosUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=256, blank=True, null=True)
    password = models.CharField(max_length=256, blank=True, null=True)


class DosResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    identifier = models.CharField(max_length=12)
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} <{self.identifier}> created at {self.created_at}'


@receiver(models.signals.post_save, sender=User)
def create_dos_user(sender, instance, *args, **kwargs):
    if not DosUser.objects.filter(user=instance).exists():
        DosUser.objects.create(user=instance)

