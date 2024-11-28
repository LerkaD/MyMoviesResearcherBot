
def check_description(movie, element):
    if element == 'name':
        if movie['name']:
            movie_name = movie['name']
        else:
            movie_name = movie['alternativeName']
        return movie_name
    elif element == 'description':
        if movie['description']:
            description = movie['description']
        elif movie['shortDescription']:
            description = movie['shortDescription']
        else:
            description = 'Нет описания'
        return description
    elif element == 'poster':
        if movie['poster']['url']:
            return movie['poster']['url']
        else:
            return 'Нет описания'
    elif element == 'budget':
        if movie['budget']['value']:
            return movie['budget']['value']
        else:
            return 'Нет описания'
    elif element == 'rating':
        if movie['rating']['kp']:
            return movie['rating']['kp']
        else:
            return 'Нет описания'
    else:
        if movie[element]:
            return movie[element]
        else:
            return 'Нет описания'
