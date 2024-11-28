import  requests
import json
from typing import List, Dict
from config_data.config import API_BASE_URL,API_KEY


def api_request(endpoint: str, headers={}) -> requests.Response:
    headers['X-API-KEY'] = API_KEY
    headers["accept"]= "application/json"
    return requests.get(
        f'{API_BASE_URL}/{endpoint}',
        headers=headers
    )

def movie_search(data: dict) -> List[str]:
    print('movie_search.api.init')
    endpoint = (f'/v1.4/movie/search?limit={data["limit"]}'
                f'&query={str(data["movie_name"])}'
                f'&genres.name={data["movie_genre"]}')
    response = api_request(endpoint)
    return response.json()

def get_movie_by_rating(data: dict):
    endpoint = (f'v1.4/movie?limit={data["limit"]}'#limit={data["limit"]}
                f'&rating.kp={data["movie_rating"]}-10'
                f'&genres.name={data["movie_genre"]}')
    #endpoint = (f'v1.4/movie?rating.kp={data["rating"]}-10')
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
    print('get_low_budget_movie')
    endpoint = (f'v1.4/movie?limit={data["limit"]}'
                f'&notNullFields=fees.usa.value&budget.value=200000000-1000000000'
                f'&genres.name={data["movie_genre"]}')
    response = api_request(endpoint)
    print(response.json())
    return response.json()

# data = {
#     "limit" : '2',
#     "movie_genre" : 'комедия'
#     }
# print(get_low_budget_movie(data))

def get_movies_by_rating(rating_from: float, rating_to: float) -> List:
    endpoint = f'/v1.4/movie?limit= 5&rating.imdb={str(rating_from)}-{rating_to}'
    response = api_request(endpoint)
    # return response.json()
    data = response.json()
    print(json.dumps(data, indent=4))
    return data




