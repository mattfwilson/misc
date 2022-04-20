lst = ['Apple', 'Pear', 'Orange']

if len(lst) < 10:
    while len(lst) < 10:
        lst.append('New Fruit')
        print(lst)
else:
    print('List is full!')