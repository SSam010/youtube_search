"""
This script prepare text for create wordcloud
This script requires a large amount of RAM (in proportion to the number of words used).
To simplify the work, the necessary tables were previously obtained from the database in the form of JSON files with the structure:
- channel(ID)
- comment
"""

import json

import emoji
import matplotlib.pyplot as plt
from stop_words import get_stop_words
from wordcloud import WordCloud


def plot_cloud(wordcloud):
    # Create plot
    plt.figure(figsize=(40, 30))
    plt.imshow(wordcloud)
    plt.axis("off")


address = input("Введите адрес JSON файла: ")

with open(address, 'r', encoding='utf-8') as f:
    # prepare text: delete emoji, empty line

    date = json.load(f)
    format_text = []
    for text in date:
        try:
            form = (''.join(char.lower() for char in text['comm'] if char not in emoji.EMOJI_DATA)).rstrip()
            if form != '':
                format_text.append(form)
        except TypeError:
            continue

# format_text = "".join(format_text)

STOPWORDS_RU = get_stop_words('russian')

wordcloud = WordCloud(width=2000,
                      height=1500,
                      random_state=1,
                      background_color='black',
                      margin=20,
                      colormap='Pastel1',
                      collocations=False,
                      stopwords=STOPWORDS_RU).generate("".join(format_text))

plot_cloud(wordcloud)

# Save picture into PNG
wordcloud.to_file('wordcloud_1.png')
