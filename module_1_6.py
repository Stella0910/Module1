my_dict = {'Sasha': 1970, 'Lena': 1971, 'Sveta': 1969, 'Vova': 1968}
print('Dict:',my_dict)
print('Existing value:', my_dict['Sveta'])
print('Not existing value:', my_dict.get('Masha', 'Такого имени нет в списке'))
my_dict.update({'Ilya': 1994,
                'Klim': 1992})
print('Deleted value:', my_dict.pop('Sasha'))
print('Modified dictionary:', my_dict)

my_set = {1, 'Sasha', 1970, 1, (1, 2, 3), 1970, 'Sveta', 1971, 1992}
print('Set:', my_set)
my_set.update(['Ilya', 1994])
my_set.discard((1, 2, 3))
print('Modified set:', my_set)