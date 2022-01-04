import requests
from pprint import pprint

def photo_vk_profile(owner_id):
    with open('token.txt', 'r') as file:
        TOKEN = file.read().strip()

    URL = 'https://api.vk.com/method/photos.get'
    PARAMS = {
        'access_token': TOKEN,
        'v': '5.131',
        'owner_id': owner_id,
        'album_id': 'profile',
        'extended': '1',
        'photo_sizes': '1'
    }
    res = requests.get(URL, params=PARAMS)
    photos_vk = {}

    for item in res.json()['response']['items']:
        date = item['date']
        name = item['likes']['count']
        photo = item['sizes'][-1]['url']
        photos_vk[name if name not in photos_vk else (str(name) + '_' + str(date))] = photo
    return photos_vk


if __name__ == '__main__':
    photo_vk_profile(input())
