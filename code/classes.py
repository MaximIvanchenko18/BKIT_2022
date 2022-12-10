class House:
    """Дом"""
    def __init__(self, id, house_num, building_num, resident_cnt, street_id):
        self.id = id
        self.house_num = house_num
        self.building_num = building_num
        self.resident_cnt = resident_cnt
        self.street_id = street_id


class Street:
    """Улица"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class HouseStreet:
    """Дома на улице"""
    def __init__(self, street_id, house_id):
        self.street_id = street_id
        self.house_id = house_id
