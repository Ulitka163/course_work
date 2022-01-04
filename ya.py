import requests
from main import photo_vk_profile
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def create_disk(self, disk_file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        headers = {'Authorization': f'OAuth {token}'}
        params = {'path': disk_file_path}
        response = requests.put(url, headers=headers, params=params)
        return response.json()

    def create_file(self, disk_file_path, filename):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload/'
        headers = {'Authorization': f'OAuth {token}'}
        params = {'path': disk_file_path, 'url': filename}
        response = requests.post(url, headers=headers, params=params)
        response.raise_for_status()
        if response.status_code == 202:
            print("Успешно")

def copy_file(token, disk_file_path, photos, number_files):
    uploader = YaUploader(token)
    uploader.create_disk(disk_file_path)
    number = 0
    for photo in photos:
        if number != number_files:
            path_to_file = photos.get(photo)
            disk_file_paths = disk_file_path + '/' + str(photo)
            uploader.create_file(disk_file_paths, path_to_file)
            number += 1
        else:
            break


if __name__ == '__main__':
    photos = photo_vk_profile(input('Введите Ваш id "ВКОНТАКТЕ": '))
    token = input('Введите токен Вашего Яндекс Диска: ')
    disk_file_path = input('Введите название папки на Вашем Яндекс Диске куда будут перенесены Ваши файлы: ')
    number = input('Введите колличество файлов: ')
    copy_file(token, disk_file_path, photos, int(number if (number != '') else 5))

