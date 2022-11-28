from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    created = models.DateTimeField(
        verbose_name=_('Created'),
        editable=False,
        auto_now_add=True
    )
    modified = models.DateTimeField(
        verbose_name=_('Last modified'),
        auto_now=True
    )

    class Meta:
        abstract = True
