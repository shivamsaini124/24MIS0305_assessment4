class AirlineReservation:

    def __init__(self, seats=10):
        self.total_seats = seats
        self.available_seats = seats
        self.bookings = {}

    def calculate_fare(self, base_fare, seat_count,
                       passenger_type, travel_class):

        fare = base_fare

        # Dynamic pricing
        if seat_count <= 2:
            fare *= 1.5
        elif seat_count <= 5:
            fare *= 1.2

        # Class
        if travel_class == "Business":
            fare *= 2
        elif travel_class == "First":
            fare *= 3
        elif travel_class != "Economy":
            raise ValueError("Invalid class")

        # Passenger
        if passenger_type == "Child":
            fare *= 0.75
        elif passenger_type == "Senior":
            fare *= 0.80
        elif passenger_type != "Adult":
            raise ValueError("Invalid passenger")

        return fare

    def book(self, passenger_id, base_fare,
             passenger_type="Adult",
             travel_class="Economy"):

        if self.available_seats <= 0:
            raise ValueError("Flight fully booked")

        if passenger_id in self.bookings:
            raise ValueError("Passenger already booked")

        fare = self.calculate_fare(
            base_fare,
            self.available_seats,
            passenger_type,
            travel_class
        )

        self.bookings[passenger_id] = fare
        self.available_seats -= 1

        return fare

    def cancel(self, passenger_id):

        if passenger_id not in self.bookings:
            raise ValueError("Invalid passenger")

        fare = self.bookings.pop(passenger_id)
        self.available_seats += 1

        refund = fare * 0.80

        return refund

    def baggage_charge(self, weight):

        if weight < 0:
            raise ValueError("Invalid baggage")

        free_limit = 15

        if weight <= free_limit:
            return 0

        return (weight - free_limit) * 100