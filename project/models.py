from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from time_tracker.models import TimeStampedModel

User = get_user_model()


class Project(TimeStampedModel):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    project_owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='projects'
    )
    participants = models.ManyToManyField(
        User,
        related_name='project_participants',
        null=True,
        blank=True
    )
    start_date = models.DateField()
    end_date = models.DateField(
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.title

    def duration(self):
        if self.end_date is None:
            return f'Project duration not set yet'
        days = (self.end_date - self.start_date).total_seconds()/86400
        return f'{days: .1f} Days'

