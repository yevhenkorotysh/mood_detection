from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import UploadSerializer
from django.shortcuts import redirect
from django.http import HttpResponse

from .api import audio_upload

# ViewSets define the view behavior.
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer

    def list(self, request):

        text = "http://mdvenv.eba-9xpeamqy.us-west-2.elasticbeanstalk.com/api/audio_list/"

        return Response(text)

    def create(self, request):
        response = audio_upload(request._request)
        response = response.data
        return Response(response)


def readme(request):
    with open('templates/readme.html', 'r') as f:
        html = f.read()
    return HttpResponse(html)