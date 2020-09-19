import requests
import os

def load_picture(picture_name, url):

    if not os.path.exists('images'):
        os.makedirs('images')

    filename = f'images\{picture_name}'

    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


load_picture('hubble.jpeg', "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg")