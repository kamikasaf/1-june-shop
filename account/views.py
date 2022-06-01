from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response

from .serializers import *

class RegistrationView(views.APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            message = """
            You are done!
            """
            return Response(message)