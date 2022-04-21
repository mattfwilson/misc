lst = ['Apple', 'Pear', 'Orange', 'Kiwi']
query = ''

query = input('What do you want to search for? ')

if len(lst) < 20:
    if "Kiwi" not in lst:
        while len(lst) < 10:
            lst.append('Kiwi')
        print('List is full!')
        for i in lst:
            if i == query:
                print(f'{i} matches your query: {query}')
            else:
                print(f'{i} does not match your query: {query}')
    else:
        while len(lst) < 10:
            lst.append('KIWI')
            print(lst)