# Space Instagram

This project uses API SpaceX which allow to download photo from launch which we want and API Hublle which allow us to download photo from hubble collection. These photo download to the folder "images" which create automatically. Then these photo preparing for publication and download to the folder "images_for_instagram" which create automatically too.  After that these photo upload to the Instagram account by using instabot.  The example of running this project presented below.
At the beginnig instabot sign in your Instagram account :
```
python Instagram_pictures.py
2020-09-25 00:16:14,473 - INFO - Instabot version: 0.117.0 Started
2020-09-25 00:16:14,474 - INFO - Not yet logged in starting: PRE-LOGIN FLOW!
2020-09-25 00:16:17,911 - INFO - Logged-in successfully as 'Your_username'!
2020-09-25 00:16:17,912 - INFO - LOGIN FLOW! Just logged-in: True
```
After that photo upload to your account one by one. The result of success operation for one photo is:

```
FOUND: w:1080 h:720 r:1.5     #w - width, h - height, r - aspect ratio of photo
2020-09-25 00:16:48,842 - INFO - Photo 'images_for_instagram/new_spacex1.jpg' is uploaded.
```

### How to install

In this project you need to get two keys: INSTAGRAM_LOGIN and INSTAGRAM_PASSWORD. As the name suggests this is the login and password from the Instagram account to which you want to upload photos.

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
