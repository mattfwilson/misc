lst = ['Apple', 'Pear', 'Orange']
query = 'Apple'

if len(lst) < 10:
    while len(lst) < 10:
        lst.append('New Fruit')
        print(lst)
    print('List is full!')
    for i in lst:
        if i == query:
            print(f'Found {query} in your list')
        else:
            print(f'No results for {query}')