class Flight:
    def __init__(self, flight_number, destination, seat_capacity):
        self.flight_number = flight_number
        self.destination = destination
        self.seat_capacity = seat_capacity
        self.booked_passengers = {}

    def book_ticket(self, passenger_name):
        # Attempt to book a ticket
        if len(self.booked_passengers) < self.seat_capacity:
            seat_number = len(self.booked_passengers) + 1
            self.booked_passengers[seat_number] = passenger_name
            return seat_number
        return None  # No available seats

    def get_details(self):
        # Get details of the flight
        return {
            'flight_number': self.flight_number,
            'destination': self.destination,
            'available_seats': self.seat_capacity - len(self.booked_passengers)
        }

    def get_report(self):
        # Generate a report of booked passengers
        report = f"Flight {self.flight_number} to {self.destination}:\n"
        for seat_number, passenger_name in self.booked_passengers.items():
            report += f"Seat {seat_number}: {passenger_name}\n"
        return report

