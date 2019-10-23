from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Return a list of APIView Features"""
        apiview_response = [
            'Hello world',
            'This app contains user auth code'
        ]
        return Response({'message': 'success', 'apiview_response': apiview_response})
