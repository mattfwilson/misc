import random

locations = {
    'Boston': {
        'Japanese': 7,
        'Mexican': 12,
        'Irish': 4,
    },
    'Seattle': {
        'Japanese': 2,
        'Mexican': 6,
        'Irish': 10,
    },
    'San Francisco': {
        'Japanese': 21,
        'Mexican': 32,
        'Irish': 11,
    },
}

def bestFood(**kwargs):
    print(kwargs['city'] + ' has the best ' + kwargs['cuisine'] + ' food.')

bestFood(city='New York City', cuisine='Lebanese')

# rand_items = random.choice(list(locations.items()))
# rand_keys = random.choice(list(locations.keys()))
# rand_values = random.choice(list(locations.values()))
# print(rand_items)
# print(rand_keys)
# print(rand_values)