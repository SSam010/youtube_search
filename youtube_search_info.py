import json
import os
from datetime import datetime
from youtubesearchpython import VideosSearch

# time now
time_now = datetime.now()
time_str = time_now.strftime("%d-%m-%Y-%H-%M-%S")
name_dir = 'search_result ' + time_str


# creating directory with name "name_dir"
os.mkdir(name_dir)

my_video_search = VideosSearch(input('Write video name: '), limit=int(input("Write number of search results: ")))
answer = my_video_search.result()

# writing the result to json
for number in answer['result']:
    number['Time search'] = str(time_now)
    with open('./' + name_dir + '/' + str(number['id']) + '.json', 'w') as f:
        json.dump(number, f, indent=4)

print("\nThe search result is placed in the directory: " + name_dir)

#тестируем тестик
a = 5
v = 4
c = a + v
