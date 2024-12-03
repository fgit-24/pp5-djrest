from django.shortcuts import render, HttpResponse
from .models import Article
from .serializers import ArticleSerializer
# from django.http import JsonResponse
from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics



class ArticleList(generics.ListCreateAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer