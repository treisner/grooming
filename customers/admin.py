from django.contrib import admin
from customers import models
admin.site.register(models.Customer)
admin.site.register(models.Breed)
admin.site.register(models.Service)
admin.site.register(models.Appointment)
admin.site.register(models.Call)
admin.site.register(models.CredentialsModel,models.CredentialsAdmin)
