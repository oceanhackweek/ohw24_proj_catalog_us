from django.db import models

# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.event_name


class Dataset(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    repo = models.URLField(blank=True)
    events = models.ManyToManyField(Event)
    datasets = models.ManyToManyField(Dataset, blank=True)

    def __str__(self):
        return self.name
