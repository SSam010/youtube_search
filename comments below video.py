import json
import os

from youtubesearchpython import *


def comment_getting():
    with open(name_dir_video_comm + '/comments.json', 'w') as vh:
        json.dump(comments.comments['result'], vh, indent=4)


search_dir = input('write directory address: ')
# getting comments below the video from video information from the selected direction
for i in os.listdir(search_dir):
    channel_directory = search_dir + '/' + i
    for video_of_selecting_channel in os.listdir(channel_directory):
        if ".json" in video_of_selecting_channel:
            name_dir_video = channel_directory + '/' + video_of_selecting_channel

            with open(name_dir_video, "r") as vch:

                data_video = json.load(vch)
                id_video_channel = data_video['id']

                # creating directory video comments
                name_dir_video_comm = channel_directory + '/' + id_video_channel

            try:
                # getting comments from video
                comments = Comments(id_video_channel)

                if name_dir_video_comm not in channel_directory:
                    os.mkdir(name_dir_video_comm)

                comment_getting()

                # check more comments in channel (default limit 20)
                while comments.hasMoreComments:
                    comments.getNextComments()
                    comment_getting()
            finally:
                continue
