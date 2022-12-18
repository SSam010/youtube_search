import json
import os
import sqlite3

import pandas

# create SQL table "channel"

dict_search = input('write address search directory: ')
connection = sqlite3.connect(input('write address library'))

dict_video = {'video_url': [], 'video_title': [], 'load_data': []}
dict_video_channel = {'channel_id': [], 'video_id': []}
dict_video_stat = {'video_id': [], 'data_query': [], 'views': []}
dict_comment = {'video_id': [], 'user_id': [], 'text': [], 'data_pub': []}
dict_user = {'name': [], 'user_id': []}
dict_user_id_table_index = {}

# create index for tables
id_channel = -1
id_video = -1
id_user = -1

for chan_dir in os.listdir(dict_search):
    id_channel += 1
    for video_from_channel in os.listdir(dict_search + '/' + chan_dir):
        if '.json' in video_from_channel:
            id_video += 1
            way_dir_chan = dict_search + '/' + chan_dir
            way_chan_video = way_dir_chan + '/' + video_from_channel

            with open(way_chan_video, 'r') as f:
                data_video = json.load(f)

                dict_video['video_url'] += [data_video['link']]
                dict_video['video_title'] += [data_video['title']]
                dict_video['load_data'] += [data_video['uploadDate']]

                dict_video_channel['channel_id'] += [id_channel]
                dict_video_channel['video_id'] += [id_video]

                dict_video_stat['video_id'] += [id_video]
                dict_video_stat['data_query'] += [data_video['Time search']]
                dict_video_stat['views'] += [int(data_video['viewCount']['text'])]

                # searching comments
                try:
                    way_video_comm = way_dir_chan + '/' + data_video['id'] + '/' + 'comments.json'
                    with open(way_video_comm, 'r') as fe:
                        data_video_comm = json.load(fe)
                        for comment in data_video_comm:

                            # User uniqueness check
                            if comment['channel'] not in dict_user_id_table_index:

                                id_user += 1
                                dict_user_id_table_index[comment['channel']] = id_user

                                dict_user['name'] += [comment['author']]
                                dict_user['user_id'] += [comment['channel']]

                                dict_comment['user_id'] += [id_user]

                            else:
                                dict_comment['user_id'] += [dict_user_id_table_index[comment['channel']]]

                            dict_comment['text'] += [comment['text']]
                            dict_comment['data_pub'] += [comment['time']]
                            dict_comment['video_id'] += [id_video]
                except:
                    print(data_video['id'] + " don't have any comments")

# sending to SQLLite

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

print('data added to the library')
