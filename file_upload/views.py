import json
from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import UploadSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework.exceptions import status
from .models import Post
from authentication.models import User


class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Post.objects.all().prefetch_related('user')

    def list(self, request):
        queryset = self.get_queryset()

        return Response(queryset.values('user_id__username', 'id', 'body', 'title'))

    def __create_user_key_map(self):
        user_data = User.objects.all()
        user_key_map = {}
        for user in user_data:
            user_key_map[user.id] = user
        return user_key_map

    def create(self, request):
        file_uploaded = request.FILES.get('file_uploaded')
        if file_uploaded:
            try:
                file_data = json.load(file_uploaded)
            except:
                raise serializers.ValidationError(
                    {'file': 'please upload valid json file'}, code=status.HTTP_400_BAD_REQUEST)

            user_key_map = self.__create_user_key_map()
            for data in file_data:
                post = Post.objects.create(
                    body=data.get('body'),
                    title=data.get('title'),
                    user_id=user_key_map.get(data['userId'])
                )
                post.save()
            return Response('file uploaded sucessfully', status=status.HTTP_201_CREATED)
