from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status

import base64

from rest_framework.response import Response

import requests
import os
from dotenv import load_dotenv

from . import plots

load_dotenv()


@csrf_exempt
def index(request):
    """Main page of web-service"""
    return render(request, 'index.html')


# def index(request):
#
#     url = 'https://api.vk.com/method/wall.get'
#     params = {
#         'owner_id': 191700058,
#         'count': 100,
#         'access_token': os.environ.get('ACCESS_TOKEN'),
#         'v': os.environ.get('VK_API_VERSION'),
#     }
#
#     response = requests.get(url, params=params).json()['response']
#     # making graph, saving is in file 'current_graph'
#     plots.wall_likes_comments_plot(response)
#     return render(request, 'index.html')


@csrf_exempt
@api_view(['GET'])
def send_to_auth(request):
    """
    This method sends user to get permanent access token
    that is necessary to use VK_api
    """

    params = {
        'client_id': os.environ.get('CLIENT_ID'),
        'redirect_uri': reverse('index'),
        'response_type': 'token',
        'scope': 'friends,offline',
    }
    return redirect('https://oauth.vk.com/authorize', params=params)


@csrf_exempt
@api_view(['POST'])
def wall(request, plot_type):
    """
    Returns image of graph of number
    of likes and comments dependency of time
    """
    url = 'https://api.vk.com/method/wall.get'
    params = {
        'owner_id': request.data.get('owner_id'),
        'offset': request.data.get('offset'),
        'count': request.data.get('count'),
        'filter': request.data.get('filter'),
        'access_token': request.data.get('access_token'),
        'v': os.environ.get('VK_API_VERSION'),
    }
    try:
        response = requests.get(url, params=params).json()['response']
        # making graph, saving is in file 'current_graph'
        plots.wall_likes_comments_plot(response, plot_type)
    except KeyError:
        pass

    graph_image = open('media/current_plot.jpeg', 'rb')
    data = {
        'image': base64.encodebytes(graph_image.read()).decode('utf-8')
    }

    return Response(data=data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(['POST'])
def stats(request, plot_type):
    """
    Returns image of graph of statistics
    of user's community during given period of time
    """

    url = 'https://api.vk.com/method/stats.get'
    params = {
        'group_id': request.data.get('group_id'),
        'app_id': request.data.get('app_id'),
        'timestamp_from': request.data.get('timestamp_from'),
        'timestamp_to': request.data.get('timestamp_to'),
        'interval': request.data.get('interval'),
        'access_token': request.data.get('access_token'),
        'v': os.environ.get('VK_API_VERSION'),
    }
    try:
        response = requests.get(url, params=params).json()['response']
        plots.stats_plot(response, plot_type)
    except KeyError:
        pass

    graph_image = open('media/current_plot.jpeg', 'rb')
    data = {
        'image': base64.encodebytes(graph_image.read()).decode('utf-8')
    }

    return Response(data=data, status=status.HTTP_200_OK)
