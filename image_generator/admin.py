"""
This file contains GeneratedImageAdmin to register model
in django admin panel
"""

from django.contrib import admin

from image_generator.models import GeneratedImage


class GeneratedImageAdmin(admin.ModelAdmin):
    """
    GeneratedImageAdmin with display fields for
    admin panel
    """
    list_display = ('id', 'prompt', 'image_url', 'created_at')

    class Meta:
        """
        Use the Meta class to specify the model
        that the GeneratedImageAdmin should work with
        """
        model = GeneratedImage


admin.site.register(GeneratedImage, GeneratedImageAdmin)
