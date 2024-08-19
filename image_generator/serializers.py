"""
This file contains GeneratedImageListSerializer and GeneratedImageCreateSerializer
to create and list generated images
"""

from rest_framework import serializers

from .messages import ERROR_MESSAGES
from .models import GeneratedImage
from .tasks import generate_image


class GeneratedImageListSerializer(serializers.ModelSerializer):
    """
    GeneratedImageListSerializer with 'to_representation' to list
    generated images
    """

    def to_representation(self, instance):
        """
        Returns the absolute URL of an image associated with the given object.
        :param instance:image object
        :return: The absolute URL of the image
        """
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if request:
            representation['image_url'] = request.build_absolute_uri(representation['image_url'])
        return representation

    class Meta:
        """
        Use the Meta class to specify the model and fields
        that the GenerateImageListSerializer should work with
        """
        model = GeneratedImage
        fields = ['id', 'image_url', 'created_at']


class GeneratedImageCreateSerializer(serializers.ModelSerializer):
    """
    GeneratedImageCreateSerializer with required field 'prompts
    to generate images.
    """
    prompts = serializers.ListField(
        child=serializers.CharField(max_length=255),
        write_only=True,error_messages=ERROR_MESSAGES['prompts']
    )

    @staticmethod
    def validate_prompts(value):
        """
        Validate that exactly 3 prompts are provided.
        :param value: prompts
        :return: value
        """
        if len(value) != 3:
            raise serializers.ValidationError(ERROR_MESSAGES['prompts']['max_limit'])
        return value

    def create(self, validated_data):
        """
        Override the create method to add custom behavior
        when generating images
        :param validated_data: validated_data
        :return: images
        """
        prompts = validated_data.get('prompts', [])
        generated_images = []

        for prompt in prompts:
            image_url = generate_image(prompt)
            generated_image = GeneratedImage.objects.create(prompt=prompt, image_url=image_url)
            generated_images.append(generated_image)

        return generated_images

    class Meta:
        """
        Use the Meta class to specify the model and fields
        that the GenerateImageCreateSerializer should work with
        """
        model = GeneratedImage
        fields = ['id', 'image_url', 'created_at', 'prompts']
        read_only_fields = ['image_url', 'created_at']
