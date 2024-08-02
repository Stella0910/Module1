immutable_var = (1, 5.2, 'string', [1, 2, 3], ['banana', 'cherry', 'orange'])
print('Immutable_var; ', immutable_var)
# immutable_var.append('end')
print("Immutable_var является кортежем. Изменять значения элементов кортежа нельзя.")
mutable_list = ['one', 'two', 'three', 10, 20.5, [21, 22, 23]]
print(mutable_list)
mutable_list[2] = 'four'
mutable_list.insert(0, 1)
print(mutable_list)
mutable_list[4] = mutable_list[4] + mutable_list[5]
mutable_list.pop(5)
print(mutable_list)
mutable_list[5] = [21, 23]
print(mutable_list)