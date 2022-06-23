import random

locations = {
    'Boston': {
        'Japanese': 7,
        'Mexican': 12,
        'Irish': 4,
        'Chinese': 17,
        'Lebanese': 2
    },
    'Seattle': {
        'Japanese': 2,
        'Mexican': 6,
        'Irish': 10,
        'Chinese': 19,
        'Lebanese': 5
    },
    'San Francisco': {
        'Japanese': 21,
        'Mexican': 32,
        'Irish': 11,
        'Chinese': 103,
        'Lebanese': 22
    },
}

rand_items = random.choice(list(locations.items()))
rand_keys = random.choice(list(locations.keys()))
rand_values = random.choice(list(locations.values()))
print(rand_items)
print(rand_keys)
print(rand_values)