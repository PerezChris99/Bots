from instapy import InstaPy
import random

session = InstaPy(username='YOUR_USERNAME', password='YOUR_PASSWORD')

session.login()

# Like and comment on close friends' posts
close_friends = ['FRIEND1', 'FRIEND2', 'FRIEND3']
session.set_do_like(enabled=True, percentage=100)
session.set_do_comment(enabled=True, percentage=100)
session.set_comments(['NICE POST!', 'GREAT JOB!', 'KEEP IT UP!'])
session.interact_by_users(close_friends, amount=10, randomize=True)

# View all stories
session.story_watch_all(amount=10, skip_top_posts=True, use_smart_hashtags=False)

# Randomly join live streams
broadcasts = session.get_live_broadcasts()
if len(broadcasts) > 0:
    broadcast = random.choice(broadcasts)
    if random.random() > 0.5:
        session.join_live_broadcast(broadcast["username"])

# Reply to messages
session.set_do_reply_to_messages(enabled=True, probability=100)
session.set_reply_to_messages(['Thanks for reaching out!', 'Hi there! How can I help you?'])
session.reply_to_messages()

# Block inactive/spam accounts
session.block_users(amount=10, block_trackers=True, style='RANDOM')

session.end()
