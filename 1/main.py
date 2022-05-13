from pprint import pp, pprint
import json
import requests

TOKEN = "2619421814940190"

def get_data_hero(search, token):
    hero = {}
    for name in search:
        url = f' https://superheroapi.com/api/'
        full_url = url + token + "/search/" + name
        r = requests.get(full_url)
        hero_json = r.json()
        hero_lst = []
        h = {}
        for current in hero_json['results']:
            if current['name'] == name:
                h['id'] = current['id']
                h['name'] = current['name']
                h['intelligence'] = current['powerstats']['intelligence']
                hero_lst.append(h)
                hero[name] = hero_lst
    return hero

if __name__ == '__main__':
    name = ['Hulk', 'Captain America', 'Thanos', ]
    result = get_data_hero(search=name, token=TOKEN + '/')
    max = 0
    for v in result.values():
        if max > int(v[0]['intelligence']):
            continue
        else:
            max = int(v[0]['intelligence'])

    for k, v in result.items():
        if max == int(v[0]['intelligence']):
            print(k, max)