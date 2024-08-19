"""
This file contains app config
"""
from django.apps import AppConfig


class ImageGeneratorConfig(AppConfig):
    """
    ImageGeneratorConfig with 'default_auto_field' and
    app name
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'image_generator'
