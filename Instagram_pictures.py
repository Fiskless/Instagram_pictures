import requests
import os
import urllib3
from PIL import Image
from instabot import Bot
from os import  listdir
from os.path import isfile
from os.path import join as joinpath
from dotenv import load_dotenv


def fetch_spacex_last_launch(spacex_url):

    response = requests.get(spacex_url)
    response.raise_for_status()
    pictures_url = response.json()['links']['flickr']['original']

    for picture_index, picture_url in enumerate(pictures_url, start=1):
        load_photo_from_internet(f'images/spacex{picture_index}.jpg', picture_url)
        convert_and_save_photo(f"images/spacex{picture_index}.jpg", f"images_for_instagram/new_spacex{picture_index}.jpg")


def fetch_hubble_pictures(hubble_id):

    response = requests.get(f'http://hubblesite.org/api/v3/image/{hubble_id}')
    response.raise_for_status()
    hubble_picture_url = response.json()['image_files'][-1]['file_url']
    expansion = hubble_picture_url.split('.')[-1]
    load_photo_from_internet(f'images/image_{hubble_id}.{expansion}', f'https:{hubble_picture_url}')
    convert_and_save_photo(f"images/image_{collection_pictures_id}.{expansion}", f"images_for_instagram/new_image_{collection_pictures_id}.jpg")


def convert_and_save_photo(path_to_picture, path_to_new_picture):

    image = Image.open(path_to_picture)
    image.thumbnail((1080, 1080))
    image_convert = image.convert('RGB')
    image_convert.save(path_to_new_picture)


def load_photo_from_internet(filename, url):
    filename = filename
    response = requests.get(url, verify = False)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':

    urllib3.disable_warnings()
    load_dotenv()
    instagram_login = os.getenv("INSTAGRAM_LOGIN")
    instagram_password = os.getenv("INSTAGRAM_PASSWORD")

    os.makedirs('images', exist_ok=True)
    os.makedirs('images_for_instagram', exist_ok=True)

    fetch_spacex_last_launch('https://api.spacexdata.com/v4/launches/5eb87ce8ffd86e000604b33c')

    response = requests.get('http://hubblesite.org/api/v3/images/wallpaper')
    response.raise_for_status()
    collection = response.json()
    for picture_index, picture_id in enumerate(collection):
        collection_pictures_id = response.json()[picture_index]['id']
        fetch_hubble_pictures(collection_pictures_id)

    bot = Bot()
    bot.login(username=instagram_login, password=instagram_password)
    my_path = "images_for_instagram"
    for picture in listdir(my_path):
        if isfile(joinpath(my_path, picture)):
            bot.upload_photo(f"images_for_instagram/{picture}", caption="Nice pic!")
