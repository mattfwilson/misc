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
        'Mexican': 29,
        'Irish': 11,
    }
}

def bestCuisine(**kwargs):
    print(kwargs['City'] + ' has a ' + kwargs['Rating'] + '/100 rated ' + kwargs['Cuisine'] + ' restaurant!')
    for key, value in kwargs.items():
        print(f'{key} = {value}')

def searchCuisine(query):
    if query in locations:
        print(f'{query} found in dictionary!')
    else:
        print('No results found.')
        
bestCuisine(City='New York City', Cuisine='Lebanese', Rating='94')
searchCuisine('Japanese')

# rand_items = random.choice(list(locations.items()))
# rand_keys = random.choice(list(locations.keys()))
# rand_values = random.choice(list(locations.values()))
# print(rand_items)
# print(rand_keys)
# print(rand_values)