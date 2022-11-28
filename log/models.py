from django.db import models
from django.contrib.auth import get_user_model

from project.models import Project
from time_tracker.models import TimeStampedModel

User = get_user_model()


class Log(TimeStampedModel):
    project = models.ForeignKey(
        Project, related_name='logs', on_delete=models.CASCADE
    )
    creator = models.ForeignKey(
        User, related_name='creator', on_delete=models.DO_NOTHING
    )
    description = models.TextField()
    time_started = models.DateTimeField()
    time_ended = models.DateTimeField()

    def time_spent_in_hours(self):
        hours = (self.time_ended - self.time_started).total_seconds()/3600
        return f'{hours: .2f} hours'
