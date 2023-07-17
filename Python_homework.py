class ParkingGarage:
    def __init__(self, num_tickets, num_parking_spaces):
        self.tickets = [i+1 for i in range(num_tickets)]
        self.parkingSpaces = [i+1 for i in range(num_parking_spaces)]
        self.currentTicket = {}

    def takeTicket(self):
        if self.tickets:
            ticket_number = self.tickets.pop(0)
            self.parkingSpaces.pop(0)
            self.currentTicket = {"ticket_number": ticket_number, "paid": False}
            print(f"Your ticket number is {ticket_number}. Please park in an available parking space.")
        else:
            print("Sorry, the parking garage is full. No tickets available.")

    def payForParking(self):
        if self.currentTicket:
            if not self.currentTicket["paid"]:
                amount = input("Enter the payment amount: ")
                if amount:
                    self.currentTicket["paid"] = True
                    print("Your ticket has been paid. You have 15 minutes to leave.")
                else:
                    print("Invalid payment amount.")
            else:
                print("Your ticket has already been paid.")
        else:
            print("No active ticket. Please take a ticket first.")

    def leaveGarage(self):
        if self.currentTicket:
            if self.currentTicket["paid"]:
                print("Thank you, have a nice day!")
                self.parkingSpaces.append(self.currentTicket["ticket_number"])
                self.tickets.append(self.currentTicket["ticket_number"])
                self.currentTicket = {}
            else:
                amount = input("Please pay for your parking ticket: ")
                if amount:
                    print("Thank you, have a nice day!")
                    self.parkingSpaces.append(self.currentTicket["ticket_number"])
                    self.tickets.append(self.currentTicket["ticket_number"])
                    self.currentTicket = {}
                else:
                    print("Invalid payment. You must pay before leaving.")
        else:
            print("No active ticket. Please take a ticket first.")


# # Example usage:
# garage = ParkingGarage(10, 10)

# garage.takeTicket()
# garage.payForParking()
# garage.leaveGarage()
