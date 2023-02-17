from datetime import datetime

from parsing_to_sql import comments_below_video as cbv
from parsing_to_sql import transfer_data_to_SQL as tds
from parsing_to_sql import youtube_video_from_chanel_v2 as yvc

time_now = datetime.now()
time_str = time_now.strftime("%d-%m-%Y-%H-%M-%S")
dir_search = 'search_result ' + time_str

SETTINGS = {
    'file_txt_address': 'channel_id.txt',
    'search_directory': dir_search,
    'db_address': 'db.sqlite3'
}

yvc.start_parsing_video(list_channel_id=SETTINGS['file_txt_address'],
                        dir_search=SETTINGS['search_directory'], time_now=time_now)

cbv.start_parsing_comments(search_dir=SETTINGS['search_directory'])

tds.transfer(list_channel_id=SETTINGS['file_txt_address'],
             dir_search=SETTINGS['search_directory'], db_address=SETTINGS['db_address'])
