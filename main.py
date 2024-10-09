from instafollower import InstaFollower
from instamanager import InstaManager
from config import USERNAME

# Initialize InstaFollower for following
insta_bot = InstaFollower()
insta_bot.login()

# Follow followers of a target account
insta_bot.find_followers()
insta_bot.follow()

# Initialize InstaManager for unfollowing and removing followers
manager = InstaManager(insta_bot.driver)

# Unfollow everyone
manager.unfollow_everyone(USERNAME)

# Remove all followers
manager.remove_all_followers(USERNAME)