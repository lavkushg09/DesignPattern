from strategy.base import VehicleStrategy

class NormalDriveCapability(VehicleStrategy):

    def drive(self):
        print('Vehicle has normal drive strategy')