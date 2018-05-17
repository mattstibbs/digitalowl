from django.contrib import admin
from ddos import models

# Register your models here.
admin.site.register(models.DosUser)
admin.site.register(models.DosResult)
