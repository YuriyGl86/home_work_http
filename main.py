import requests
import pprint

#  Task 1

heroes_list = ['Hulk', 'Captain America', 'Thanos']


def most_intelligence_superheroes(heroes_list):
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    heroes_dict = {}
    for hero in heroes_list:
        for i in response.json():
            if i['name'] == hero:
                heroes_dict[hero] = i['powerstats']['intelligence']
    heroes_list_sorted = sorted(heroes_list, key=lambda x: heroes_dict[x])
    return heroes_list_sorted[-1]


print(f'Самый умный супергерой из {", ".join(heroes_list)} - это {most_intelligence_superheroes(heroes_list)}')

#  Task 2

new_folder_path = '/netology/tests/'
file_path = '/netology/tests/test_file_for_upload.txt'
file = 'test_file_for_upload.txt'
TOKEN = ''


class Yandex:

    def __init__(self, token):
        self.__token = token

    def get_headers(self):
        return {'Content-Type': 'application/json', 'Authorization': f'OAuth {self.__token}'}

    def get_new_folder(self, folder_path):
        link = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {'path': folder_path}
        response = requests.put(link, headers=headers, params=params)
        if response.status_code == 201:
            print("Success")

    def get_link_for_upload(self, path, owerwrite=True):
        link = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': path, 'owerwrite': owerwrite}
        response = requests.get(link, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, path, file):
        upload_link = self.get_link_for_upload(path)['href']
        with open(file, 'rb') as data:
            response = requests.put(upload_link, data=data)
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


yandex = Yandex(TOKEN)
yandex.get_new_folder(new_folder_path)
yandex.upload_file_to_disk(file_path, file)