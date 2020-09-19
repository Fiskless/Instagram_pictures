import requests
import os

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


#
# fetch_spacex_last_launch('https://api.spacexdata.com/v4/launches/5eb87ce8ffd86e000604b33c')
#


response = requests.get('http://hubblesite.org/api/v3/image/1')
response.raise_for_status()
hubble_pictures = response.json()['image_files']
for image_index, image_url in enumerate(hubble_pictures):
    print(hubble_pictures[image_index]['file_url'])



def picture_expansion(url):
    expansion = url.split('.')[-1]
    print(expansion)




