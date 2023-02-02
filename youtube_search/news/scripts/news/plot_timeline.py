import datetime

import plotly.graph_objs as go
from plotly.io import to_html
from pathlib import Path

from ...models import VidDate0, VidDate1, VidDate2

DIR = Path(__file__).resolve().parent.parent.parent


def create_timeline():
    for file_chen in (VidDate0, VidDate1, VidDate2):
        if file_chen == VidDate0:
            name_channel = 'BadComedian'
            name_channel_eng = 'BadComedian'
        if file_chen == VidDate1:
            name_channel = 'вДудь'
            name_channel_eng = 'VDut'
        if file_chen == VidDate2:
            name_channel = 'ещёнепознер'
            name_channel_eng = 'pozner'

        date_pub = [j['load_data'] for j in file_chen.objects.values('load_data')]

        # Working with JSON files
        """
import json
import os        
    for file_chen in os.listdir(f'{DIR}/scripts/news/timeline'):
        if file_chen == 'vid_date0.json':
            name_channel = 'BadComedian'
            name_channel_eng = 'BadComedian'
        if file_chen == 'vid_date1.json':
            name_channel = 'вДудь'
            name_channel_eng = 'VDut'
        if file_chen == 'vid_date2.json':
            name_channel = 'ещёнепознер'
            name_channel_eng = 'pozner'

        with open(f'{DIR}/scripts/news/timeline/{file_chen}', 'r') as e:
            date_pub = []
            data = json.load(e)
            for u in data:
                date_pub += [u['load_data']]"""

        # sort list by date
        date_pub.sort()

        # first and last dates
        date_start = datetime.datetime.strptime(date_pub[0], "%Y-%m-%d")
        date_end = datetime.datetime.strptime(date_pub[-1], "%Y-%m-%d")

        table_date = [[], []]

        # We are creating a list table with two included lists.
        # First list: a range of dates in 1-day increments from start to end.
        # The second list is the number of videos uploaded that day.
        while True:
            if date_start <= date_end:
                table_date[0] += [str(date_start.date())]
                table_date[1] += [date_pub.count(str(date_start.date()))]

                date_start += datetime.timedelta(days=1)
            else:
                break

        # create table for plot, where first elem = number of period, second elem = number of videos for this period

        def period_plot(period):
            global table_date_with_period
            table_date_with_period = [[], []]
            days = 0
            point = 0
            while True:
                if days + period <= len(table_date[0]):
                    table_date_with_period[0] += [point]
                    point += 1
                    number_of_video = sum(table_date[1][days:days + period])
                    days += period
                    table_date_with_period[1] += [number_of_video]
                elif days <= len(table_date[0]):
                    # last point, if last point + period > date_end

                    table_date_with_period[0] += [point]
                    differ = len(table_date[0]) - period
                    number_of_video = sum(table_date[1][days:differ])
                    table_date_with_period[1] += [number_of_video]
                    break
                else:
                    break

        period_plot(1)

        trace_list = [go.Scatter(visible=True, x=table_date_with_period[0],
                                 y=table_date_with_period[1],
                                 mode='lines+markers', name='f(x)=x<sup>2</sup>')]

        num_steps = [14, 28, 50, 75, 100, 180, 365]
        for i in num_steps:
            period_plot(i)
            trace_list.append(
                go.Scatter(visible=False, x=table_date_with_period[0],
                           y=table_date_with_period[1],
                           mode='lines+markers', name='f(x)=x<sup>2</sup>'))

        fig = go.Figure(data=trace_list)

        steps = []
        for i in range(len(num_steps)):
            # Hide all traces
            step = dict(
                label=str(num_steps[i]),
                method='restyle',
                args=['visible', [False] * len(fig.data)],
            )
            # Enable trace we want to see
            step['args'][1][i] = True

            # Add step to step list
            steps.append(step)

        sliders = [dict(
            currentvalue={"prefix": "Колличество дней за шаг: ", "font": {"size": 20}},
            pad={"b": 10, "t": 50},
            steps=steps,
        )]
        fig.update_layout(showlegend=False, title=f'{name_channel}', xaxis_title="Дата, шаг",
                          yaxis_title="Число загрузок, шт")
        fig.layout.sliders = sliders

        # Create plot html
        html_str = to_html(fig)
        with open(f'{DIR}/templates/news/timeline_{name_channel_eng}.html', 'w') as ht:
            ht.write(html_str)


create_timeline()
