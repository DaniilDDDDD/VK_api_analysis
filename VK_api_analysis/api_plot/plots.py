import pandas as pd
import matplotlib.pyplot as plt
import time


def wall_likes_comments_plot(data, plot_type='line'):
    """
    Parse response data of posts of a single user and make plot using it
    Plot saves as 'current_plot.png'
    """

    col_names = ['date', 'likes', 'comments', 'reposts']
    items = []
    for d in data['items']:
        item = [
            time.ctime(d['date'])[4:],
            d['likes']['count'],
            d['comments']['count'],
            d['reposts']['count'],
        ]
        items.append(item)

    df = pd.DataFrame(data=items, columns=col_names)

    df.plot(x='date', y=['likes', 'comments', 'reposts'], kind=plot_type)

    plt.tight_layout()
    plt.savefig('media/current_plot.jpeg', dpi=225)


def stats_plot(data, plot_type='bar'):
    """
    Parse response data of statistics of a user's community and make plot using it.
    Plot saves as 'current_plot.png'
    """

    col_names = [
        'period',
        'views',
        'visitors',
        'likes',
        'subscribes',
        'unsubscribes'
    ]
    items = []

    for d in data:
        default = {
            'likes': 0,
            'subscribed': 0,
            'unsubscribed': 0
        }
        activities = d.get('activity', default)
        item = [
            f'From {time.ctime(d["period_from"])[4:]}',
            d['visitors']['views'],
            d['visitors']['visitors'],
            activities.get('likes', 0),
            activities.get('subscribed', 0),
            activities.get('unsubscribed', 0)
        ]
        items.append(item)

    df = pd.DataFrame(data=items, columns=col_names)

    df.plot(
        x='period',
        y=[
            'views',
            'visitors',
            'likes',
            'subscribes',
            'unsubscribes'
        ],
        kind=plot_type
    )
    plt.tight_layout()
    plt.savefig('media/current_plot.jpeg', dpi=225)


def posts_analisis(data):


    # сюда запиши результаты анализа в json формате
    result = {

    }

    return result
