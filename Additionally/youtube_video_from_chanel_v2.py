import json
import os
import re
from datetime import datetime

import requests as req
from youtubesearchpython import *


# getting videos from channel and recording into JSON files
def video_getting():
    for video_from_channel in playlist.videos:
        with open(directory + '/' + channel_name + '/' + video_from_channel['id'] + '.json', 'w') as vh:
            # getting information about channel videos
            video_info = Video.getInfo(video_from_channel['link'], mode=ResultMode.json)

            # add time search in json
            video_info['Time search'] = str(time_now)

            json.dump(video_info, vh, indent=4)


list_channel_url = input('write address of text file with url channels: ')

# Create search directory
time_now = datetime.now()
time_str = time_now.strftime("%d-%m-%Y-%H-%M-%S")
directory = 'search_result ' + time_str
os.mkdir(directory)

# search by id channel
with open(list_channel_url, "r") as lcu:
    for channel_id in lcu:
        playlist = Playlist(playlist_from_channel_id(channel_id))

        # creating channel directory
        channel_name = playlist.videos[0]['channel']['name']
        os.mkdir(directory + '/' + channel_name)

        # check more videos in channel (default limit 100)
        while playlist.hasMoreVideos:
            playlist.getNextVideos()

        video_getting()
        print('search results are saved in the directory "' + channel_name + '"')
