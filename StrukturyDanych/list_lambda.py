names = ['John Johnson', 'Alicja Policja', 'Wladimir Wladymirowicz']


def get_sub_name(name, part):
    first_name = name.split()[part]
    return first_name

fist_names = [get_sub_name(name,0) for name in names]
last_names = [get_sub_name(name,1) for name in names]

first_names_lambda = [(lambda name: name.split()[0])(name) for name in names]
last_names_lambda = [(lambda name: name.split()[1])(name) for name in names]

fist_names_genetaror = [name.split()[0] for name in names]
last_names_generator = [name.split()[1] for name in names]

print(fist_names_genetaror, last_names_generator)