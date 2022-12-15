import json
import os
import requests as req
import re
from datetime import datetime
from youtubesearchpython import *

# getting videos from channel
def video_getting():
    for video_from_channel in playlist.videos:
        with open(name_dir_channel + '/' + video_from_channel['id'] + '.json', 'w') as vh:
            video_info = Video.getInfo(video_from_channel['link'], mode=ResultMode.json)
            # add time search in json
            video_info['Time search'] = str(time_now)
            json.dump(video_info, vh, indent=4)


time_now = datetime.now()
directory = input('write directory address: ')

# getting channel id from video information from the selected direction
for name_file in os.listdir(directory):
    if ".json" in name_file:
        with open(directory + '/' + name_file, "r") as f:
            data_video = json.load(f)
            id_channel = data_video['channel']['id']
            name_channel = data_video['channel']['name']
            # creating name directory channel
            name_dir_channel = directory + '/' + name_channel

            # check if the directory exists. Create a directory if it doesn't exist

            if name_channel not in os.listdir(directory):

                # creating directory channel
                os.mkdir(name_dir_channel)

                playlist = Playlist(playlist_from_channel_id(id_channel))

                # check more videos in channel (default limit 100)
                while playlist.hasMoreVideos:
                    playlist.getNextVideos()
                video_getting()
                print('search results are saved in the directory "' + name_channel + '"')
            else:
                print('Channel directory "' + name_channel + '" already created')
