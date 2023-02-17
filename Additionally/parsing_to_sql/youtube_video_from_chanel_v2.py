import json
import os

from youtubesearchpython import *


def start_parsing_video(list_channel_id, dir_search, time_now):
    os.mkdir(dir_search)
    # search by id channel
    with open(list_channel_id, "r") as lcu:
        for channel_id in lcu:
            playlist = Playlist(playlist_from_channel_id(channel_id))

            # creating channel directory
            channel_name = playlist.videos[0]['channel']['name']
            os.mkdir(dir_search + '/' + channel_name)

            # check more videos in channel (default limit 100)
            while playlist.hasMoreVideos:
                playlist.getNextVideos()

            # getting videos from channel and recording into JSON files
            for video_from_channel in playlist.videos:
                with open(dir_search + '/' + channel_name + '/' + video_from_channel['id'] + '.json', 'w') as vh:
                    # getting information about channel videos
                    video_info = Video.getInfo(video_from_channel['link'], mode=ResultMode.json)

                    # add time search in json
                    video_info['Time search'] = str(time_now)

                    json.dump(video_info, vh, indent=4)

            print(f'Parsing video results are saved in the directory "{channel_name}"')
