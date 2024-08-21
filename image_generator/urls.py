"""
This file contains URL patterns for image_generator
It uses a DefaultRouter to generate views
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from image_generator.views.generate_images import GeneratedImageViewSet

router = DefaultRouter()

router.register('generate', GeneratedImageViewSet, basename='generate')

urlpatterns = [
    path('', include(router.urls)),
]
