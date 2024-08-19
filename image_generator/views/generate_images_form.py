import os

import requests

from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.dateparse import parse_datetime
from django.utils.timezone import localtime

from image_generator.forms.generate_images import GenerateImagesForm
from image_generator.messages import SUCCESS_MESSAGES, ERROR_MESSAGES

base_url = os.getenv('BASE_URL')


def list_generated_images(request):
    """
    To list generate images
    """

    if request.method == 'GET':
        response = requests.get(base_url)
        data = response.json()

        for image in data:
            image['created_at'] = localtime(parse_datetime(image['created_at']))
        context = {
            'generated_images': data,
        }

        return render(request, 'list_generated_images.html', context)


def create_generate_images(request):
    """
    To generate images and redirect to listing page
    """
    if request.method == 'POST':
        form = GenerateImagesForm(request.POST)
        if form.is_valid():
            prompts = form.cleaned_data['prompts']
            response = requests.post(base_url, data={'prompts': prompts})
            if response.status_code == 201:
                messages.success(request, SUCCESS_MESSAGES['images']['generated'])
                return redirect('list_generated_images')
        else:
            messages.error(request, ERROR_MESSAGES['common']['errors'])
    else:
        form = GenerateImagesForm()

    return render(request, 'generate_images.html', {'form': form})
