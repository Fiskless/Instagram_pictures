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


response = requests.get('https://api.spacexdata.com/v4/launches/5eb87ce8ffd86e000604b33c')
response.raise_for_status()
link_shorten = response.json()['links']['flickr']['original']
for l in link_shorten:
    print(l)


