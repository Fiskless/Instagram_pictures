import requests
import os
import urllib3
from PIL import Image


urllib3.disable_warnings()


def fetch_spacex_last_launch(url_from_spacexdata):

    response = requests.get(url_from_spacexdata)
    response.raise_for_status()
    picture_url = response.json()['links']['flickr']['original']

    for picture_index, url_picture in enumerate(picture_url):
        if not os.path.exists('images'):
            os.makedirs('images')
        filename = f'images/spacex{picture_index+1}.jpg'
        response = requests.get(url_picture)
        response.raise_for_status()
        with open(filename, 'wb') as file:
            file.write(response.content)


def hubble_pictures_load(id):

    response = requests.get(f'http://hubblesite.org/api/v3/image/{id}')
    response.raise_for_status()
    hubble_picture_url = response.json()['image_files'][-1]['file_url']
    expansion = hubble_picture_url.split('.')[-1]
    if not os.path.exists('images'):
        os.makedirs('images')
    filename = f'images/image_{id}.{expansion}'
    response = requests.get(f'https:{hubble_picture_url}', verify = False)
    response.raise_for_status()
    with open(filename, 'wb') as file:
        file.write(response.content)
    if not os.path.exists('images_for_Instagram'):
        os.makedirs('images_for_Instagram')
    image = Image.open(f"images/image_{collection_pictures_id}.{expansion}")
    image.thumbnail((1080, 1080))
    image_convert = image.convert('RGB')
    image_convert.save(f"images_for_Instagram/new_image_{collection_pictures_id}.jpg")



response = requests.get('http://hubblesite.org/api/v3/images/stsci_gallery')
response.raise_for_status()
collection = response.json()
for picture_index, pictures_id in enumerate(collection):
    collection_pictures_id = response.json()[picture_index]['id']
    hubble_pictures_load(collection_pictures_id)
