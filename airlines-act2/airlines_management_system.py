from flight import Flight

class AirlinesManagementSystem:
    def __init__(self):
        # Initialize the airlines management system
        self.flights = {}  # Dictionary to store all flights indexed by flight number

    def add_flight(self, flight_number, destination, seat_capacity):
        # Add a new flight to the system
        if flight_number not in self.flights:  # Check if the flight already exists
            self.flights[flight_number] = Flight(flight_number, destination, seat_capacity)  # Create a new Flight object
            print(f"Flight {flight_number} to {destination} added successfully.")
        else:
            print(f"Flight {flight_number} already exists.")

    def book_ticket(self, flight_number, passenger_name):
        # Book a ticket for a passenger on a specific flight
        if flight_number in self.flights:  # Check if the flight exists
            flight = self.flights[flight_number]  # Retrieve the flight object
            seat_number = flight.book_ticket(passenger_name)  # Attempt to book a ticket
            if seat_number:
                print(f"Ticket booked for {passenger_name} on flight {flight_number}. Seat number: {seat_number}.")
            else:
                print(f"No available seats on flight {flight_number}.")
        else:
            print(f"Flight {flight_number} does not exist.")

    def view_flight(self, flight_number):
        # View details of a specific flight
        if flight_number in self.flights:  # Check if the flight exists
            flight = self.flights[flight_number]  # Retrieve the flight object
            details = flight.get_details()  # Get flight details
            print(f"Flight {flight_number} to {details['destination']}: {details['available_seats']} seats available.")
        else:
            print(f"Flight {flight_number} does not exist.")

    def generate_report(self, flight_number):
        # Generate a report for a specific flight
        if flight_number in self.flights:  # Check if the flight exists
            flight = self.flights[flight_number]  # Retrieve the flight object
            report = flight.get_report()  # Get flight report
            print(f"Report for flight {flight_number}: {report}")
        else:
            print(f"Flight {flight_number} does not exist.")
