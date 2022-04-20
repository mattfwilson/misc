lst = ['Apple', 'Pear', 'Orange']
query = ''

query = input('What do you want to search for? ')

if len(lst) < 10:
    while len(lst) < 10:
        lst.append('Apple')
        print(lst)
    print('List is full!')
    for i in lst:
        if i == query:
            print(f'{i} matches your query: {query}')
        else:
            print(f'{i} does not match your query: {query}')