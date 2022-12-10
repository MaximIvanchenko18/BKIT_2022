# one_to_many - связь 1-М
def house_num_more_3(one_to_many):
    return list(filter(lambda x: x[0] > 3, one_to_many))
