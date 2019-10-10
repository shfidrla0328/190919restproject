from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
import requests
import json


# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    url = "https://kapi.kakao.com/v1/translation/translate" 
    queryString = {"query":"당신은 나를 사랑합니까?", "src_lang":"kr", "target_lang":"en"}
    header = {"Authorization": "KakaoAK 1155da90c9368c49bc216b5aa562f432"}
    r = requests.get(url, headers=header, params=queryString)
    print(json.loads(r.text))