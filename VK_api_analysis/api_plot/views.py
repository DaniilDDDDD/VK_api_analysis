from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status

import base64, time

from rest_framework.response import Response

import requests
import os
from dotenv import load_dotenv

from . import plots

load_dotenv()


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
        response = requests.get(url, params=params).json()
        # making graph, saving is in file 'current_graph.jpeg'
        plots.wall_likes_comments_plot(response['response'], plot_type)

    except KeyError:
        pass

    graph_image = open('media/current_plot.jpeg', 'rb')
    data = {
        'image': 'data:image/png;base64,'
                 + base64.encodebytes(graph_image.read()).decode('utf-8')
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
        'timestamp_from': request.data.get('timestamp_from', time.time()-157680000),
        'timestamp_to': request.data.get('timestamp_to', time.time()),
        'interval': request.data.get('interval', 'week'),
        'intervals_count': request.data.get('intervals_count', 5),
        'access_token': request.data.get('access_token'),
        'v': os.environ.get('VK_API_VERSION'),
    }
    try:
        response = requests.get(url, params=params).json()
        plots.stats_plot(response['response'], plot_type)
    except KeyError:
        pass

    graph_image = open('media/current_plot.jpeg', 'rb')
    data = {
        'image': 'data:image/png;base64,'
        + base64.encodebytes(graph_image.read()).decode('utf-8')
    }

    return Response(data=data, status=status.HTTP_200_OK)
