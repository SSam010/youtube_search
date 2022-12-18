import pandas
from youtubesearchpython import Channel
import sqlite3


# create SQL table "channel"

id_txt = input('write address of id.txt: ')
dict_channel = {'channel_url': [], 'channel_name': [], 'channel_desc': []}

# recording information in a dictionary
with open (id_txt, 'r') as f:
    for channel_id in f:
        channel_info = Channel.get(channel_id.rstrip())
        dict_channel['channel_url'] += [channel_info['url']]
        dict_channel['channel_name'] += [channel_info['title']]
        dict_channel['channel_desc'] += [channel_info['description']]

# sending to SQLLite
table_channel = pandas.DataFrame.from_dict(dict_channel)
connection = sqlite3.connect('base_youtube.db')
table_channel.to_sql('channel', connection, if_exists='append', index_label='id')

print('channels added to the library')
