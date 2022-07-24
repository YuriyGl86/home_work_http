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