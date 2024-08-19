"""
This file contains utils functions that can be 
used throughout the project 
"""

from .tasks import generate_image


def generate_images(prompts):
    """
    To genearate images 
    :param prompts: 
    :return: 
    """
    tasks = [generate_image.delay(prompt) for prompt in prompts]
    results = [task.get() for task in tasks]
    return results
