from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UploadViewSet

router = DefaultRouter()
router.register('', UploadViewSet, basename='fileupload_view')
urlpatterns = [
    path('upload/',
         UploadViewSet.as_view({'post': 'create', 'get': 'list'}), name='upload'),
]
urlpatterns += router.urls
