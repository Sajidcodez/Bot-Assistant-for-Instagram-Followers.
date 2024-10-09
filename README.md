# Bot-Assistant-for-Instagram-Followers.
## Overview

This Instagram Follower Bot automates the process of logging into an Instagram account, finding followers of a target account, and following them automatically. Additionally, the bot can unfollow all accounts or remove all followers.

## Features
- Logs in to Instagram automatically using credentials.
- Fetches followers from a specified account and follows them.
- Unfollows all accounts you're following.
- Removes all followers from your account.
- Handles common exceptions like prompts to "Unfollow" or cookie warnings.

## Requirements
- Python 3.7+
- Google Chrome Browser
- ChromeDriver (Ensure that the version matches your Chrome browser version)
- Selenium

## Installation
### 1. Clone the Repository

```bash
- git clone https://github.com/YOUR_USERNAME/instagram-follower-bot.git
  cd instagram-follower-bot

- pip install -r requirements.txt
- Update the config.py file with your a choice of your instagram account, includes it's 
  username and password and the target account to follow.
- Run the main file and enjoy!
- To unfollow everyone, manager.unfollow_everyone("YOUR_USERNAME"). Enter your username
- To remove all followers, manager.remove_all_followers("YOUR_USERNAME"). Enter your username.
