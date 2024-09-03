from django.contrib import admin

# Register your models here.
from .models import Event, Dataset, Project


admin.site.register(Event)
admin.site.register(Dataset)
admin.site.register(Project)
