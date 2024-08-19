"""
This file contains celery tasks
"""

import base64
import os
from io import BytesIO

import requests
from PIL import Image
from celery import shared_task

from chaotixai import settings


@shared_task
def generate_image(prompt):
    """
    task to generate images using stability api
    :param prompt: prompt
    :return: generated images
    """
    url = os.getenv('STABILITY_API')
    api_key = os.getenv('STABILITY_API_KEY')

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    payload = {
        "text_prompts": [
            {
                "text": prompt,
            }
        ]
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        response_json = response.json()
        artifacts = response_json.get('artifacts')
        for artifact in artifacts:
            if artifact['finishReason'] == "SUCCESS":
                image_base64 = artifact["base64"]
                image_data = base64.b64decode(image_base64)
                image = Image.open(BytesIO(image_data))

                project_media_directory = os.path.join(settings.BASE_DIR, 'media')
                os.makedirs(project_media_directory, exist_ok=True)

                image_filename = f"{prompt.replace(' ', '_')}.png"
                image_path = os.path.join(project_media_directory, image_filename)
                image.save(image_path)
                image_url = f"/media/{image_filename}"
                return image_url
    else:
        return None
