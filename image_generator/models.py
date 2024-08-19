"""
This file contains models
"""

from django.db import models


class GeneratedImage(models.Model):
    """
    Custom GeneratedImage with fields : 'prompt'
    'image_url', 'created_at' and default manager
    """
    prompt = models.CharField(max_length=255)
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    class Meta:
        """
        Use the Meta class to specify the database table
        for GeneratedImage model
        """
        db_table = 'GeneratedImage'
