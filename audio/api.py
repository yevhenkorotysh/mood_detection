from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import AudioFile
from .serializers import AudioFileSerializer

import mutagen
import math

ALLOWED_FORMATS = ['mp3', 'wav']

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def audio_list(request):
    audio_obj = AudioFile.objects.all()
    audio_file_json = AudioFileSerializer(audio_obj, many=True).data
    return Response(audio_file_json)

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def audio_details(request, id):
    audio_obj = AudioFile.objects.filter(id=id)
    if audio_obj.exists():
        audio_file_json = AudioFileSerializer(audio_obj[0], many=False).data
        return Response(audio_file_json)
    else:
        return Response({"error": "file does not exist",
                         "id": id,
                         })

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def audio_upload(request):
    files = request.FILES

    if len(files) == 0:
        return Response({"error": "file is not attached"})

    for each_file in files:


        file = files[each_file]
        # check file format

        file_name = file.name
        file_format = file_name.split('.')[-1].lower()
        if file_format not in ALLOWED_FORMATS:
            audio_file_json = {"error": "this file format is not allowed",
                             "file_name": file_name,
                             "allowed_audio_formats": ALLOWED_FORMATS}
            return Response(audio_file_json)


        # read audio file metadata
        audio_info = mutagen.File(file).info

        # check audio duration in seconds, so we can save it to database
        duration_seconds = math.ceil(audio_info.length)

        if duration_seconds > 30:
            audio_file_json = {"error": "This audio file is too long. You may upload audio files up to 30 seconds",
                             "file_name": file_name,
                             "duration": duration_seconds}

        else:
            audio_file = AudioFile.objects.create(audiofile=file, duration=duration_seconds)
            audio_file_json = AudioFileSerializer(audio_file, many=False).data


    return Response(audio_file_json)


