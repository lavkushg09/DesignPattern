class Vehicle:
    def __init__(self, strategy_instance , wheel=4):
        self.wheels = wheel
        self.strategy_instance = strategy_instance

    def __str__(self):
        return f'Vehicle with {self.wheels} wheels'
    
    def get_number_of_wheels(self):
        return self.wheels