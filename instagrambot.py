from instapy import InstaPy
import random

session = InstaPy(username='YOUR_USERNAME', password='YOUR_PASSWORD')

session.login()

# Like posts with a certain hashtag
session.like_by_tags(['HASHTAG'], amount=10)

# Post a photo
session.upload_photo(
    'PHOTO_PATH', 
    caption='YOUR_CAPTION', 
    upload_id=None, 
    thumbnail=None, 
    action_delays=None, 
    comment=False, 
    remove_Captionhashtags=False, 
    ignore_if_contains=None, 
    use_video=False, 
    video_code=None
)

# Comment on a post
session.set_do_comment(enabled=True, percentage=50)
session.set_comments(['YOUR_COMMENT'])
session.like_by_tags(['HASHTAG'], amount=10)

# Join or leave a live stream randomly
broadcasts = session.get_live_broadcasts()
if len(broadcasts) > 0:
    broadcast = random.choice(broadcasts)
    if random.random() > 0.5:
        session.join_live_broadcast(broadcast["username"])
    else:
        session.leave_live_broadcast(broadcast["broadcast_id"])

# Follow an account
session.follow_by_username('USERNAME')

# Unfollow an account
session.unfollow_users(amount=10, allFollowing=False, style='RANDOM', unfollow_after=42 * 60 * 60, sleep_delay=600)

# View available stories
session.story_watch('USERNAME')

session.end()
