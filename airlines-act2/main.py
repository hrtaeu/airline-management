from airlines_management_system import AirlinesManagementSystem

def main():
    # Main function to run the Airlines Management System
    system = AirlinesManagementSystem()  # Create an instance of the Airlines Management System

    while True:  # Loop to allow continuous user interaction
        action = input("What would you like to do? (add/book/view/report/exit): ").strip().lower()  # Get user action
        if action == "add":  # If user wants to add a flight
            flight_number = input("Enter flight number: ")  # Get flight number
            destination = input("Enter destination: ")  # Get destination
            seat_capacity = int(input("Enter seat capacity: "))  # Get seat capacity
            system.add_flight(flight_number, destination, seat_capacity)  # Add flight to the system
        elif action == "book":  # If user wants to book a ticket
            flight_number = input("Enter flight number: ")  # Get flight number
            passenger_name = input("Enter passenger name: ")  # Get passenger name
            system.book_ticket(flight_number, passenger_name)  # Book ticket
        elif action == "view":  # If user wants to view flight details
            flight_number = input("Enter flight number: ")  # Get flight number
            system.view_flight(flight_number)  # View flight details
        elif action == "report":  # If user wants to generate a report
            flight_number = input("Enter flight number: ")  # Get flight number
            system.generate_report(flight_number)  # Generate flight report
        elif action == "exit":  # If user wants to exit the system
            print("Thank you for using the Airlines Management System!")  # Exit message
            break  # Exit the loop
        else:
            print("Invalid action! Please try again.")  # Message for invalid action


if __name__ == "__main__":
    main()  # Run the main function to start the application
