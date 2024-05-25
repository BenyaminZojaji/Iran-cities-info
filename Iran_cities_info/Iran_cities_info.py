import os
import json
# import check


def get_completeData(lang: str='en'): 
    '''
    Get complete json data.
    lang = en | fa
    '''
    file_path = os.path.join('Iran_cities_info', 'assets', f'iran_cities_en.json') # need fix
    print(os.path.isfile(file_path))
    print(os.path.isfile(os.path.join('assets', 'iran_cities_en.json')))
    print(os.path.isfile(os.path.join('iran_cities_en.json')))
    print(os.path.isfile('Iran_cities_info/assets/iran_cities_en.json'))
    print(os.path.isfile('assets/iran_cities_en.json'))
    print(os.path.isfile('iran_cities_en.json'))
    print(os.path.isfile('Iran_cities_info/iran_cities_en.json'))
    with open(file_path) as f:
        return json.load(f)


def get_all_province_names(lang: str='en'):
    '''
    Get names of all the provinces of Iran
    lang = en | fa
    '''
    data = get_completeData(lang=lang)
    result = list(map(lambda x: x['name'], data))
    return result


def get_coordinates(_city: str='', lang: str='en'):
    '''
    Get coordinates of given city.

    lang = en | fa
    '''
    if not empty_argument(_city):
        return {'error': 'empty argument'}
    
    data = get_completeData(lang=lang)
    for state in data:
        for city in state['cities']:
            if city['name'] == _city:
                return city['latitude'], city['longitude']


def search_province(_province: str='', lang: str='en'):
    '''
    Search by province, get full data of given province.

    lang = en | fa
    '''
    if not empty_argument(_province):
        return {'error': 'empty argument'}
    
    data = get_completeData(lang=lang)
    for state in data:
        if state['name'] == _province:
            return state


def search_center(_center: str='', lang: str='en'):
    '''
    Search by center of a province, get full data of given city.

    lang = en | fa
    '''
    if not empty_argument(_center):
        return {'error': 'empty argument'}
    
    data = get_completeData(lang=lang)
    for state in data:
        if state['center'] == 'Shiraz':
            return state


def empty_argument(argument):
    return False if argument=='' else True

## ---------- This part is only for my classroom assignment, It will be remove in future ----------
import wikipedia 
def wiki(search: str):
    result = wikipedia.page(search) 
    return result.summary

import pyjokes
def joke():
    return pyjokes.get_joke()

## ---------- ---------- ---------- ---------- ---------- ---------- ---------- ---------- ----------

print(get_completeData())