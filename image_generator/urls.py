"""
This file contains URL patterns for image_generator
It uses a DefaultRouter to generate views
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from image_generator.views.generate_images import GeneratedImageViewSet
from image_generator.views.generate_images_form import list_generated_images, create_generate_images

router = DefaultRouter()

router.register('generate', GeneratedImageViewSet, basename='generate')

urlpatterns = [
    path('', include(router.urls)),
    path('list-images/', list_generated_images, name='list_generated_images'),
    path('generate-images/', create_generate_images, name='generate_images'),

]
