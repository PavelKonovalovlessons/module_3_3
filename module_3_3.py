def print_params(a=1, b='строка', c=True):
    print(a, b, c)


if print_params is None:
    print_params = []
    print_params.append(1, 2, 3)
    print(print_params)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = (False, 123, 'Правда')
print_params(*values_list)
values_dict = {'a': 21, 'b': 'второй', 'c': True}
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)