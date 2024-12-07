from http.client import error

import  requests
import json
from typing import List
from config_data.configuration import API_BASE_URL,API_KEY


def api_request(endpoint: str, headers={}):
    # headers['X-API-KEY'] = API_KEY
    # headers["accept"]= "application/json"
    # response =  requests.get(f'{API_BASE_URL}/{endpoint}',headers=headers)
    # print(response,response.status_code)
    # if response.status_code == 200 :
    #     return
    # else:
    #     return response
    headers['X-API-KEY'] = API_KEY
    headers["accept"] = "application/json"
    response =  requests.get(
        f'{API_BASE_URL}/{endpoint}',
        headers=headers
    )
    # if response.status_code == 200:
    if response['total'] == 0:
        return response
    else:
        return None

def movie_search(data: dict) -> List[str]:
    print('movie_search.api.init')
    endpoint = (f'/v1.4/movie/search?limit={data["limit"]}'
                f'&query={str(data["movie_name"])}'
                f'&genres.name={data["movie_genre"]}')
    response = api_request(endpoint)
    return response.json()

def get_movie_by_rating(data: dict):
    print('get_movie_by_rating')
    endpoint = (f'v1.4/movie?limit={data["limit"]}'#limit={data["limit"]}
                f'&rating.kp={data["movie_rating"]}-10'
                f'&genres.name={data["movie_genre"]}')
    response = api_request(endpoint)
    return response.json()


def get_low_budget_movie(data: dict):
    print('get_low_budget_movie')
    endpoint = (f'v1.4/movie?limit={data["limit"]}'
                f'&&notNullFields=fees.usa.value&budget.value=1-1000000000'
                f'&genres.name={data["movie_genre"]}')
    response = api_request(endpoint)
    print(response.json())
    return response.json()

def get_high_budget_movie(data: dict):
    endpoint = (f'v1.4/movie?limit={data["limit"]}'
                f'&notNullFields=fees.usa.value&budget.value=200000000-1000000000'
                f'&genres.name={data["movie_genre"]}')
    response = api_request(endpoint)
    return response.json()
