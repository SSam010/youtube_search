from youtube_comment_downloader import *


def get_comments_from_directory(search_dir):
    # Selecting channel directory
    for channel_name in os.listdir(search_dir):
        channel_directory = os.path.join(search_dir, channel_name)

        # Selecting channel video
        for video_of_selecting_channel in os.listdir(channel_directory):

            # Work only with video (all videos are recorded in JSON files)
            if ".json" in video_of_selecting_channel:
                name_dir_video = os.path.join(channel_directory, video_of_selecting_channel)

                # Getting video information
                with open(name_dir_video, "r") as vch:
                    data_video = json.load(vch)
                    id_video_channel = data_video['id']
                    video_url = data_video['link']
                    # creating directory video comments
                    name_dir_video_comm = os.path.join(channel_directory, id_video_channel)

                # Getting comments below the video from video information from the selected direction
                downloader_com = YoutubeCommentDownloader()
                comments = downloader_com.get_comments_from_url(video_url, language='en')

                data_comments = [comment for comment in comments]

                # Check for comments and create comment directory
                if len(data_comments) != 0:
                    os.mkdir(name_dir_video_comm)
                    # Recording comments into JSON file
                    with open(name_dir_video_comm + '/comments.json', 'w') as vh:
                        json.dump(data_comments, vh, indent=4)

        print(f'Comments from the channel "{channel_name}" received.')


