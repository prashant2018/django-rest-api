from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api import models
from profiles_api import permissions


class HelloApiView(APIView):
    """Test API View"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView Features"""
        apiview_response = [
            'Hello world',
            'This app contains user auth code'
        ]
        return Response({'message': 'success', 'apiview_response': apiview_response})

    def post(self, request):
        """Create hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello ' + name
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'Put'})

    def patch(self, request, pk=None):
        """Handles a partial update of an object"""
        return Response({'method': 'Patch'})

    def delete(self, request, pk=None):
        """Delete an object"""
        return Response({'method': 'Delete'})


class HelloViewSet(viewsets.ViewSet):
    """Test APIViewset"""

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return hello msg"""
        viewset_list = [
            "Uses actions (list, create, update, partial_update)",
            "Automatically maps to URLs using Routers",
            "Provides more functionality with less code"
        ]
        return Response({'message': 'Hello', 'viewset_list': viewset_list})

    def create(self, request):
        """Create new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = 'Hello ' + name
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle getting object by ID"""
        return Response({'method': 'GET'})

    def update(self, request, pk=None):
        """Handle update object by ID"""
        return Response({'method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating partial object by ID"""
        return Response({'method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle delete object by ID"""
        return Response({'method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)


class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authtoken"""

    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handles Create,read,update profile feed"""
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSereailizer
    queryset = models.ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        """sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)
