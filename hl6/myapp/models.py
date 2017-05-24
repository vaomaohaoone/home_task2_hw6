from django.db import models
import datetime
from django import utils


class RoadMap(models.Model):
    rd_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATE_CHOICES = (('in_progress', 'in_progress'), ('ready', 'ready'),)
    title = models.CharField(max_length=100)
    state = models.CharField(max_length=11, choices=STATE_CHOICES, default='in_progress')
    estimate = models.DateField(default=utils.timezone.now)
    my_id = models.AutoField(primary_key=True)
    road_map = models.ForeignKey(RoadMap, related_name='tasks')

    class Meta:
        ordering = ['state', 'estimate']





