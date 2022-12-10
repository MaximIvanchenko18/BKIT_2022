from operator import itemgetter


# many_to_many - связь М-М
def data_sorted_by_house_num(many_to_many):
    return sorted(many_to_many, key=itemgetter(0, 1))
