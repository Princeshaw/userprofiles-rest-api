from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    """Test API View"""
    def get(self,request,format = None):
        """Returns a list APIView geatures"""
        an_apiview = ['Uses HTTP methods as function(get,post,patch,put,delete)','Is similar to traditional Django View',
                      'gives you the most control over you application logic','Is mapped manually to urls',]
        return Response({'message':'Hello','an_apiview':an_apiview})