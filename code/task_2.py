from operator import itemgetter
from data_connections import streets


# one_to_many - связь 1-М
def streets_with_min_resident_cnt(one_to_many):
    streets_min_resident_cnt = []
    for s in streets:
        street_resident_cnt = [(s_n, r_c) for h_n, b_n, r_c, s_n in one_to_many if s.name == s_n]
        # Если на улице есть дома
        if len(street_resident_cnt) > 0:
            streets_min_resident_cnt.append(min(street_resident_cnt))
    return sorted(streets_min_resident_cnt, key=itemgetter(1), reverse=True)
