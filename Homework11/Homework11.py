class Vehicle:
    engine = 'engine'
    where_used = 'ground / water / air'
    color = 'color'
    size = 'dimensions'
    cost = 'amount of cost'
    max_speed = 'amount of max_speed'
    brand = 'brand'
    model = 'model'
    engine_on = False  # Or True

    def engine_start(self):
        self.engine_on = True

    def engine_stop(self):
        self.engine_on = False


class Car(Vehicle):
    wheels = 4
    radio = 'radio'
    steering_wheel = 'steering wheel'
    conditioner = 'conditioner'
    horsepower = 'amount of horsepower'
    video_camera = 'videocamera'
    radio_on = False  # Or True

    def radio_turn_on(self):
        self.radio_on = True

    def radio_turn_off(self):
        self.radio_on = False


class Truck(Car):
    torque = 'torque'
    max_weight_of_cargo = 'max weight of cargo'
    additional_wheels = 'amount of additional wheels'


class Airplane(Vehicle):
    wheels = 2
    wings = 2
    max_weight = 'max weight'
    radio_set = 'radio set'


class Helicopter(Vehicle):
    blades = 'amount of blades'
    radio_set = 'radio set'


class Ship(Vehicle):
    sails = 'sails'
    anchor = 'anchor'
