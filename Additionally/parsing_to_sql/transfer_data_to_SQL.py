import json
import os
import sqlite3

import pandas
from youtubesearchpython import Channel


def transfer(list_channel_id, dir_search, db_address):
    connection = sqlite3.connect(db_address)

    # Create dictionaries for SQL"
    dict_video = {'video_url': [], 'video_title': [], 'load_data': []}
    dict_video_channel = {'channel_id': [], 'video_id': []}
    dict_video_stat = {'video_id': [], 'data_query': [], 'views': []}
    dict_comment = {'video_id': [], 'user_id': [], 'text': [], 'data_pub': []}
    dict_user = {'name': [], 'user_id': []}
    dict_channel = {'channel_url': [], 'channel_name': [], 'channel_desc': []}
    dict_user_id_table_index = {}

    # Create index for tables
    id_channel = -1
    id_video = -1
    id_user = -1

    # Recording information about channels
    with open(list_channel_id, 'r') as channel_ids:
        for channel_id in channel_ids:
            channel_info = Channel.get(channel_id.rstrip())
            dict_channel['channel_url'] += [channel_info['url']]
            dict_channel['channel_name'] += [channel_info['title']]
            dict_channel['channel_desc'] += [channel_info['description']]

    # Opening channel directories
    for chan_dir in os.listdir(dir_search):
        # Channel indexing
        id_channel += 1

        # Get video data
        for video_from_channel in os.listdir(os.path.join(dir_search, chan_dir)):
            # Checking the file type(video data is stored only in files JSON, not in directories
            if '.json' in video_from_channel:
                # Video indexing
                id_video += 1
                way_dir_chan = os.path.join(dir_search, chan_dir)
                way_chan_video = os.path.join(way_dir_chan, video_from_channel)

                # Recording information about channel video
                with open(way_chan_video, 'r') as video_data_json:
                    data_video = json.load(video_data_json)

                    dict_video['video_url'].append(data_video['link'])
                    dict_video['video_title'].append(data_video['title'])
                    dict_video['load_data'].append(data_video['uploadDate'])

                    dict_video_channel['channel_id'].append(id_channel)
                    dict_video_channel['video_id'].append(id_video)

                    dict_video_stat['video_id'].append(id_video)
                    dict_video_stat['data_query'].append(data_video['Time search'])
                    dict_video_stat['views'].append(int(data_video['viewCount']['text']))

                    # Searching comments
                    try:
                        way_video_comm = os.path.join(way_dir_chan, data_video['id'], 'comments.json')
                        with open(way_video_comm, 'r') as video_comm_json:
                            data_video_comm = json.load(video_comm_json)
                            for comment in data_video_comm:

                                # User uniqueness check
                                if comment['channel'] not in dict_user_id_table_index:

                                    # recording information about video comment
                                    id_user += 1
                                    dict_user_id_table_index[comment['channel']] = id_user

                                    dict_user['name'].append(comment['author'])
                                    dict_user['user_id'].append(comment['channel'])

                                    dict_comment['user_id'].append(id_user)

                                else:
                                    dict_comment['user_id'].append(dict_user_id_table_index[comment['channel']])

                                # recording information about video comment
                                dict_comment['text'].append(comment['text'])
                                dict_comment['data_pub'].append(comment['time'])
                                dict_comment['video_id'].append(id_video)
                    except:
                        print(f"{data_video['id']} don't have any comments")

    # Sending to SQLLite
    table_video = pandas.DataFrame.from_dict(dict_video)
    table_video.to_sql('video', connection, if_exists='append', index_label='id')

    table_video_chan = pandas.DataFrame.from_dict(dict_video_channel)
    table_video_chan.to_sql('video_channel_content', connection, if_exists='append', index_label='id')

    table_video_stat = pandas.DataFrame.from_dict(dict_video_stat)
    table_video_stat.to_sql('video_stat', connection, if_exists='append', index_label='id')

    table_user = pandas.DataFrame.from_dict(dict_user)
    table_user.to_sql('user', connection, if_exists='append', index_label='id')

    table_comments = pandas.DataFrame.from_dict(dict_comment)
    table_comments.to_sql('comment', connection, if_exists='append', index_label='id')

    table_channel = pandas.DataFrame.from_dict(dict_channel)
    table_channel.to_sql('channel', connection, if_exists='append', index_label='id')

    print('Data added to the library')
