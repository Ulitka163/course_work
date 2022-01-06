import requests
import json
import datetime
from pprint import pprint

now = datetime.datetime.now()
now_date = now.strftime("%d-%m-%Y")

def photo_vk_profile(owner_id, album, count):
    with open('token.txt', 'r') as file:
        TOKEN = file.read().strip()

    if not owner_id.isdigit():
        url = 'https://api.vk.com/method/utils.resolveScreenName'
        params = {'access_token': TOKEN, 'screen_name': owner_id, 'v': '5.131'}
        result = requests.get(url, params)
        owner_id = result.json()['response']['object_id']

    URL = 'https://api.vk.com/method/photos.get'
    PARAMS = {
        'access_token': TOKEN,
        'v': '5.131',
        'owner_id': owner_id,
        'album_id': album,
        'extended': '1',
        'photo_sizes': '1',
        'count': count
    }
    res = requests.get(URL, params=PARAMS)
    photos_vk = {}
    photos_vk_json = []

    for item in res.json()['response']['items']:
        date = item['date']
        name = item['likes']['count']
        photo = item['sizes'][-1]['url']
        size = item['sizes'][-1]['type']
        photos_vk[str(name) + '.jpg' if str(name) + '.jpg' not in photos_vk else (str(name) + '_' + str(date) + '.jpg')] = photo
        photos_vk_json.append({'file_name': str(name) + '.jpg' if str(name) + '.jpg' not in (i['file_name'] for i in photos_vk_json) else (str(name) + '_' + str(date) + '.jpg'), 'size': size})

    with open(f'{str(owner_id)}_{now_date}.json', 'w') as f:
        json.dump(photos_vk_json, f)

    return photos_vk


if __name__ == '__main__':
    pprint(photo_vk_profile(input(), input(), input()))