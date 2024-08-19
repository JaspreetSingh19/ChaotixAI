"""
This file containsGeneratedImageViewSet with create() , list() and
retrieve()
"""

from rest_framework import viewsets, status
from rest_framework.response import Response

from image_generator.messages import SUCCESS_MESSAGES
from image_generator.models import GeneratedImage
from image_generator.serializers import GeneratedImageListSerializer, GeneratedImageCreateSerializer


class GeneratedImageViewSet(viewsets.ModelViewSet):
    """
    The GeneratedImageViewSet handles 'create', 'list' and 'retrieve'
    It provides a serializer class for each action
    """
    queryset = GeneratedImage
    serializer_class = GeneratedImageListSerializer

    def get_queryset(self):
        """
        The get_queryset method returns a queryset of GeneratedImage Model objects
        It orders the queryset based on the ID of the objects.
        :return: GeneratedImage objects
        """
        queryset = self.queryset.objects.all().order_by('-id')
        return queryset

    def get_serializer_class(self):
        """
        The get_serializer_class returns a serializer class based on the action being performed.
        For 'create' action, it returns GeneratedImageCreateSerializer,
        and for all other actions, it returns the default serializer, GeneratedImageListSerializer.
        :return: serializer class
        """
        serializer_class = self.serializer_class
        if self.action == 'create':
            return GeneratedImageCreateSerializer
        return serializer_class

    def list(self, request, *args, **kwargs):
        """
        The list retrieves all instances of the GeneratedImage model.
        serializes them using the serializer returned by the get_serializer() method,
        and returns the serialized data in a Response object with a status code of 200 (OK).
        :return: GeneratedImage instances
        """
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """
        This method retrieves a single instance of the GeneratedImage model
        using the provided primary key (pk).
        It then serializes the instance using the serializer defined for the view and
        returns the serialized data in a Response object with a status code of 200 (OK).
        :return: GeneratedImage instance
        """
        serializer = self.get_serializer(self.get_object())
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        This method creates a new instance of the GeneratedImage model using validated serializer data
        If the data is valid, it creates a new instance and
        returns a success response with a status code of 201.
        If the data is invalid, it returns an error response with a status code of 400.
        :return: GeneratedImage object
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            generated_images = serializer.create(serializer.validated_data)
            image_serializer = self.get_serializer(generated_images, many=True)
            return Response({'message': SUCCESS_MESSAGES['images']['generated'],
                             'data': image_serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

