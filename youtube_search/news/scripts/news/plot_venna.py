import mpld3
from matplotlib import pyplot as plt
from matplotlib_venn import venn3_unweighted

# Working with a database. Available in the extended version of the database.
"""
from ...models import VideoChannelContent, Comment


#getting channel video
VCC0 = VideoChannelContent.objects.values("video").filter(channel=0)
VCC1 = VideoChannelContent.objects.values("video").filter(channel=1)
VCC2 = VideoChannelContent.objects.values("video").filter(channel=2)
comment = Comment.objects.all()

# Getting unique users for channel 0
channel0 = comment.filter(video__in=[i['video'] for i in VCC0])
channel0 = channel0.values('user').distinct()

# Getting unique users for channel 1
channel1 = comment.filter(video__in=[i['video'] for i in VCC1])
channel1 = channel1.values('user').distinct()

# Getting unique users for channel 2
channel2 = comment.filter(video__in=[i['video'] for i in VCC2])
channel2 = channel2.values('user').distinct()

# Unique user matches across channels
channel01 = channel0.intersection(channel1)
channel02 = channel0.intersection(channel2)
channel12 = channel1.intersection(channel2)
channel012 = channel12.intersection(channel0)

channel_0 = channel0.count()
channel_1 = channel1.count()
channel_2 = channel2.count()
channel_01 = channel01.count()
channel_02 = channel02.count()
channel_12 = channel12.count()
channel_012 = channel012.count()

chd_01 = channel_01 - channel_012
chd_02 = channel_02 - channel_012
chd_12 = channel_12 - channel_012
chd_0 = channel_0 - channel_012 - chd_01 - chd_02
chd_1 = channel_1 - channel_012 - chd_01 - chd_12
chd_2 = channel_2 - channel_012 - chd_12 - chd_02
"""

# Preset Data to Build

channel_0 = 1086936
channel_1 = 2204044
channel_2 = 147869
channel_01 = 327346
channel_02 = 21968
channel_12 = 73873
channel_012 = 17816

chd_01 = channel_01 - channel_012
chd_02 = channel_02 - channel_012
chd_12 = channel_12 - channel_012
chd_0 = channel_0 - channel_012 - chd_01 - chd_02
chd_1 = channel_1 - channel_012 - chd_01 - chd_12
chd_2 = channel_2 - channel_012 - chd_12 - chd_02

fig = plt.figure()
venn3_unweighted(subsets=(chd_0, chd_1, chd_01, chd_2, chd_02, chd_12, channel_012),
                 set_labels=('BadComedian', 'вДудь', 'ещёнепознер'),
                 set_colors=("orange", "blue", "red"), alpha=0.7,
                 )

# Create plot html
html_str = mpld3.fig_to_html(fig)


def create_venna():
    with open('D:/Projects/pythonDjango/youtube_search/news/templates/news/plot_venna.html', 'w') as ht:
        ht.write(html_str)
