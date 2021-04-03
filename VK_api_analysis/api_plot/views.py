from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from wsgiref.util import FileWrapper


import requests
import os

from . import plots


def index(request):
    """Main page of web-service"""
    return render(request, 'index.html')


@api_view(['GET'])
def send_to_auth(request):
    """
    This method sends user to get permanent access token that is necessary to use VK_api
    """

    params = {
        'client_id': os.environ.get('CLIENT_ID'),
        'redirect_uri': reverse('index'),
        'response_type': 'token',
        'scope': 'friends,offline',
    }
    return redirect('https://oauth.vk.com/authorize', params=params)


@api_view(['POST'])
def comments_likes(request):
    """
    Returns image of graph of number of likes and comments dependency of time
    """
    url = 'https://api.vk.com/method/wall.get'
    params = {
        'owner_id': request.data.get('owner_id'),
        'count': request.data.get('count'),
        'filter': request.data.get('filter'),
        'access_token': request.data.get('access_token'),
        'v': os.getenv('VK_API_VERSION'),
    }
    posts = requests.get(url, params=params).json()['response']['items']

    # making graph, saving is in file 'current_graph'
    plots.make_graph(posts)

    graph_image = open('current_graph', 'rb')

    response = HttpResponse(FileWrapper(graph_image), content_type='image/jpeg')
    return response
