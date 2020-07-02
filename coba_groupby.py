from itertools import groupby

g = groupby([1, 1, 2, 2, 2, 3])

for key, grp in g:
    print('{}: {}'.format(key, list(grp)))


data = [{'name': 'Alan', 'age': 34},
        {'name': 'Catherine', 'age': 34},
        {'name': 'Betsy', 'age': 29},
        {'name': 'Alan', 'age': 13}]

data_sorted = sorted(data, key=lambda i:i['name'])

print(data_sorted)

grouped_data = groupby(data_sorted, key=lambda x: x['name'])

for key, grp in grouped_data:
    print('{}: {}'.format(key, list(grp)))