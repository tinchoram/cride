"""django models utilities"""

# Django
from django.db import models


class CRideModel(models.Model):
    """Comparte Ride base model.

    CrideModel acts as an abstract base class from which every
    otrer model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the object was created
        + modified (DateTime): Store the datetime the object was modified
    """

    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='the datetime the object was created'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='the datetime the object was modified'
    )

    class Meta:
        """Meta options"""
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']
