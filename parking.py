class ParkingManagement:

    def __init__(self):
        self.slots = {
            "Bike": 5,
            "Car": 5,
            "SUV": 3,
            "Truck": 2,
            "EV": 2
        }

        self.vehicles = {}

    def entry(self, vehicle_number, vehicle_type):

        if vehicle_number in self.vehicles:
            raise ValueError("Duplicate vehicle")

        if vehicle_type not in self.slots:
            raise ValueError("Invalid vehicle type")

        if self.slots[vehicle_type] <= 0:
            raise ValueError("Parking full")

        self.slots[vehicle_type] -= 1

        self.vehicles[vehicle_number] = {
            "type": vehicle_type
        }

        return True

    def exit(
        self,
        vehicle_number,
        hours,
        lost_ticket=False,
        peak=False,
        ev_charging=False
    ):

        if vehicle_number not in self.vehicles:
            raise ValueError("Invalid vehicle")

        vehicle_type = self.vehicles[vehicle_number]["type"]

        rates = {
            "Bike": 20,
            "Car": 40,
            "SUV": 60,
            "Truck": 80,
            "EV": 40
        }

        if hours <= 0:
            raise ValueError("Invalid duration")

        fee = rates[vehicle_type] * hours

        if peak:
            fee *= 1.5

        if lost_ticket:
            fee += 500

        if ev_charging and vehicle_type == "EV":
            fee += 100

        self.slots[vehicle_type] += 1
        del self.vehicles[vehicle_number]

        return fee