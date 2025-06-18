import emoji
s = 'All you need is love'
if 'love' in s:
    print(emoji.emojize(":red_heart:", variant="emoji_type"))
else:
    print('💔')
