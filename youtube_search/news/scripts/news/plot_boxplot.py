import plotly.graph_objs as go
from plotly.io import to_html
from plotly.subplots import make_subplots

from ...models import Chen0, Chen1, Chen2


def create_boxplot():
    for i in (Chen0, Chen1, Chen2):
        if i == Chen0:
            name_channel = 'BadComedian'
            name_channel_eng = 'BadComedian'
        if i == Chen1:
            name_channel = 'вДудь'
            name_channel_eng = 'VDut'
        if i == Chen2:
            name_channel = 'ещёнепознер'
            name_channel_eng = 'pozner'

        views = [j['views'] for j in i.objects.values('views')]
        com = [j['com'] for j in i.objects.values('com')]
        user = [j['us'] for j in i.objects.values('us')]

        fig = make_subplots(rows=1, cols=3)
        fig.add_trace(go.Box(y=views, name='Просмотры'), 1, 1)
        fig.add_trace(go.Box(y=com, name='Комментарии'), 1, 2)
        fig.add_trace(go.Box(y=user, name='Уник. пользователи'), 1, 3)
        fig.update_layout(showlegend=False, title=f'{name_channel}')

        # Create plot html
        html_str = to_html(fig)
        with open(f'D:/Projects/pythonDjango/youtube_search/news/templates/news/{name_channel_eng}.html', 'w') as ht:
            ht.write(html_str)


create_boxplot()

# Working with JSON files
"""
import json
import os
def create_boxplot():
    for i in os.listdir('D:/Projects/pythonDjango/youtube_search/news/scripts/news/boxplot'):
        if i == 'chen0.json':
            name_channel = 'BadComedian'
            name_channel_eng = 'BadComedian'
        if i == 'chen1.json':
            name_channel = 'вДудь'
            name_channel_eng = 'VDut'
        if i == 'chen2.json':
            name_channel = 'ещёнепознер'
            name_channel_eng = 'pozner'

        with open(f'D:/Projects/pythonDjango/youtube_search/news/scripts/news/boxplot/{i}', 'r') as e:
            chennel_data = json.load(e)

        views = []
        com = []
        user = []

        for j in chennel_data:
            views.append(j["views"])
            com.append(j['com'])
            user.append(j['us'])

        fig = make_subplots(rows=1, cols=3)
        fig.add_trace(go.Box(y=views, name='Просмотры'), 1, 1)
        fig.add_trace(go.Box(y=com, name='Комментарии'), 1, 2)
        fig.add_trace(go.Box(y=user, name='Уник. пользователи'), 1, 3)
        fig.update_layout(showlegend=False, title=f'{name_channel}')
        html_str = to_html(fig)

        with open(f'D:/Projects/pythonDjango/youtube_search/news/templates/news/{name_channel_eng}.html', 'w') as ht:
            ht.write(html_str)
create_boxplot()"""
