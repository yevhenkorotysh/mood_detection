from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField

from audio.models import *

class AudioFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioFile
        fields =[
                'id',
                'file_name',
                'duration',
                'mood_detected',
                'created_at',
                ]

# Serializers define the API representation.
class UploadSerializer(Serializer):
    file_uploaded = FileField()
    class Meta:
        fields = ['file_uploaded']