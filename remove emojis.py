import json

import emoji
"""
This script removes all emojis in json file and creates a new txt file without them.
"""
with open('words/com_chen2.json', 'r', encoding='utf-8') as f:
    date = json.load(f)
    format_text = []
    for text in date:
        try:
            format_text += [''.join(char for char in text['comm'] if char not in emoji.EMOJI_DATA)]
        except TypeError:
            continue


format_text = "".join(format_text)
with open('words/form_text2.txt', 'w', encoding='utf-8') as tx:
    tx.write(format_text)
