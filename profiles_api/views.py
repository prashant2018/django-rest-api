from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


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
