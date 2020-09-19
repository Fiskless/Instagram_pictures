import requests
import os


def load_picture(picture_name, url):

    if not os.path.exists('images'):
        os.makedirs('images')

    filename = f'images/{picture_name}'

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def fetch_spacex_last_launch(url_from_spacexdata):

    response = requests.get(url_from_spacexdata)
    response.raise_for_status()
    picture_url = response.json()['links']['flickr']['original']

    for picture_index, url_picture in enumerate(picture_url):
        load_picture(f'spacex{picture_index+1}.jpg', url_picture)


fetch_spacex_last_launch('https://api.spacexdata.com/v4/launches/5eb87ce8ffd86e000604b33c')

