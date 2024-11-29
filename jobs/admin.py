from django.contrib import admin
from jobs import models
# Register your models here.


admin.site.register(models.Category)
admin.site.register(models.Job)
admin.site.register(models.Application)