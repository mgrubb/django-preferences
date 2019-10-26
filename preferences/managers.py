from django.conf import settings
from django.db import models

class SingletonManager(models.Manager):
    """
    Returns a single preferences object.
    """
    def get_queryset(self):
        """
        Return the first preferences object.
        If preferences do not exist create it.
        """

        queryset = super(SingletonManager, self).get_queryset()

        if not queryset.exists():
            # Create object (for current site) if it doesn't exist.
            obj = self.model.objects.create()

        return queryset
