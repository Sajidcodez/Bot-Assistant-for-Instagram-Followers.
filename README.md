# InstaBot

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

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
### Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/instagram-follower-bot.git
cd instagram-follower-bot
pip install -r requirements.txt

Configuration
Update the config.py file with your Instagram account credentials, including its username and password, and the target account to follow.

Usage
To unfollow everyone:

manager.unfollow_everyone("YOUR_USERNAME")
To remove all followers:

manager.remove_all_followers("YOUR_USERNAME")
Run the main file and enjoy!

Contributing
Contributions are welcome! Please open an issue or submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License. See the LICENSE file for details.

You can update your README.md file with the above content to include the recommended improvements.

