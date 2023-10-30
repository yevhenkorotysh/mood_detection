from django.urls import path, include
from rest_framework import routers
from .api import *
from .views import UploadViewSet, readme

router = routers.DefaultRouter()
router.register(r'upload', UploadViewSet, basename="upload")

urlpatterns = [
                path('audio_list/', audio_list),
                path('audio_upload/', audio_upload),
                path('audio_details/<int:id>/', audio_details),
                path('', include(router.urls)),
                path('readme/', readme),

]