from base.vehicle import Vehicle

class MotorCycle(Vehicle):

    def __init__(self, strategy_ins, wheel=2):
        super().__init__(strategy_ins, wheel)


    def drive(self):
        self.strategy_instance.drive()
