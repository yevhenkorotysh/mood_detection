from django.db import models
import random
CHIOCES = [
    ['Happy', 'Happy'],
    ['Sad', 'Sad'],
    ['Calm', 'Calm'],
]

class AudioFile(models.Model):
    file_name = models.TextField('file_name', null=True, blank=True)
    audiofile = models.FileField(upload_to="audiofile/", default=None, blank=True)
    mood_detected = models.TextField(null=True, blank=True, choices=CHIOCES)
    duration = models.IntegerField(null=True, default=None, blank=True)
    created_at = models.DateTimeField('created_at', auto_now_add=True)

    def save(self, *args, **kwargs):
        self.file_name = self.audiofile.name
        self.mood_detected = random.choices(CHIOCES)[0][0]
        super().save(*args, **kwargs)
