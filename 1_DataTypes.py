class Car:
    max_speed = 100
    min_speed = 0
    weight = 4079
    is_on = False
    condition = 'A'

    def __init__(self, max_speed, min_speed, weight, is_on, condition):
        self.max_speed = max_speed
        self.min_speed = min_speed
        self.weight = weight
        self.is_on = is_on
        self.condition = condition
