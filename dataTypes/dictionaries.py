my_dict = {
    'k1': 1,
    'k2': 2,
    'k3': 3,
    'k4': {
        '4a': 'nested value'
    }
}

print(
    my_dict.keys(), 
    my_dict.values(),
    my_dict.items(),
    my_dict['k1'],
    my_dict['k4']['4a'],
)