from classes import *
# Улицы
streets = [
    Street(1, 'Веселая'),
    Street(2, 'Замечательная'),
    Street(3, 'Великолепная'),

    # Для связи М-М
    Street(11, 'Потрясная (старое название)'),
    Street(22, 'Неповторимая (старое название)'),
    Street(33, 'Отличная (старое название)')
]
# Дома
houses = [
    House(1, 5, 2, 100, 1),
    House(2, 2, 1, 125, 2),
    House(3, 10, 3, 232, 2),
    House(4, 7, 1, 260, 3),
    House(5, 4, 1, 170, 3),
    House(6, 3, 4, 200, 3)
]
# Дома на улицах (для связи М-М)
houses_streets = [
    HouseStreet(1, 1),
    HouseStreet(2, 2),
    HouseStreet(2, 3),
    HouseStreet(3, 4),
    HouseStreet(3, 5),
    HouseStreet(3, 6),

    HouseStreet(11, 1),
    HouseStreet(22, 2),
    HouseStreet(22, 3),
    HouseStreet(33, 4),
    HouseStreet(33, 5),
    HouseStreet(33, 6)
]

# Связь 1-М
one_to_many = [
    (h.house_num, h.building_num, h.resident_cnt, s.name)
    for h in houses
    for s in streets
    if h.street_id == s.id
]

# Связь М-М
many_to_many = [
    (h.house_num, h.building_num, h.resident_cnt, [s.name for s in streets if s.id == h_s.street_id][0])
    for h in houses
    for h_s in houses_streets
    if h.id == h_s.house_id
]
