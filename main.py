import os
import time
from datetime import datetime

import pyfiglet

COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_MAGENTA = "\033[95m"
COLOR_CYAN = "\033[36m"
COLOR_GOLD = "\033[33m"
COLOR_RESET = "\033[0m"


def clear_terminal():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    print(COLOR_YELLOW + pyfiglet.figlet_format("\nPARKING    LOT") + COLOR_RESET)


def user_answer():
    """
    Prompts user to select an option and returns their selection.
    Calls clear_terminal() before and after errors to clear the screen.
    Uses time.sleep(5) after errors to pause briefly.
    """
    while True:
        try:
            answer = int(
                input(
                    COLOR_GOLD
                    + "Select an option to continue:\n"
                    + "[1] Grab a ticket\n"
                    + "[2] Pay ticket\n"
                    + "[0] Exit\n"
                    + "--> "
                    + COLOR_RESET
                )
            )
            if answer == 0:
                clear_terminal()
                print(COLOR_BLUE + "Thank you for your visit!" + COLOR_RESET)
                time.sleep(5)
                break
            if 1 <= answer <= 3:
                return answer
            else:
                clear_terminal()
                print(
                    COLOR_RED
                    + "Invalid option. Please select a number between 1 and 3."
                    + COLOR_RESET
                )
                time.sleep(5)
                clear_terminal()
        except ValueError:
            clear_terminal()
            print(
                COLOR_RED + "Invalid input. Please enter a valid number." + COLOR_RESET
            )
            time.sleep(5)
            clear_terminal()


class garage:
    def __init__(self):
        self.available_tickets = [num for num in range(1, 11)]
        self.ticket_records = {}  # Dictionary to store ticket issuance date and time

    def issue_ticket(self):
        if self.available_tickets:
            ticket_number = self.available_tickets.pop(0)
            now = datetime.now()  # Get the current date and time
            self.ticket_records[ticket_number] = now  # Store the issuance date and time
            return ticket_number
        else:
            return None

    def return_ticket(self, ticket_number):
        if 1 <= ticket_number <= 10:
            self.available_tickets.append(ticket_number)
            del self.ticket_records[ticket_number]

    def interface(self):
        while True:
            clear_terminal()
            print(
                COLOR_CYAN + "Parking available: ",
                len(self.available_tickets),
                "\n" + COLOR_RESET,
            )
            answer_input = user_answer()
            if answer_input == 1:
                ticketID = self.issue_ticket()
                if ticketID is not None:
                    clear_terminal()
                    print(
                        COLOR_CYAN + f"Grab your ticket\n" f"Ticket ID:",
                        ticketID,
                        COLOR_RESET,
                    )
                    current_time = datetime.now()
                    print(
                        COLOR_MAGENTA + f"Time: {current_time}\n\n"
                        f"Have a good day!" + COLOR_RESET
                    )
                    time.sleep(1)
                else:
                    clear_terminal()
                    print(COLOR_RED + "No spaces available", COLOR_RESET)
                    time.sleep(5)
            elif answer_input == 2:
                clear_terminal()
                ticket_number = int(input(f"Enter your ticket number\n" f"-->"))
                if ticket_number in self.ticket_records:
                    current_time = datetime.now()
                    duration = current_time - self.ticket_records[ticket_number]
                    total_time = duration.total_seconds() / 60
                    amount = total_time * 0.25
                    amount_round = round(amount, 2)
                    clear_terminal()
                    print(
                        COLOR_BLUE + f"Ticket ID: {ticket_number}\n"
                        f"Parking duration: ",
                        duration,
                        f"\nTotal charge: $",
                        amount_round,
                        COLOR_RESET + COLOR_GREEN + "\n\nSystem is broken\n"
                        "Hit enter to continue",
                        "\nHave a good day",
                        COLOR_RESET,
                    )
                    input("Pay with bitcoin only, minimum required is 1")
                    clear_terminal()
                    print(
                        COLOR_RED + "Ticket has been paid.\n"
                        "You have 15 minutes to leave",
                        COLOR_RESET,
                    )
                    time.sleep(5)
                    self.return_ticket(ticket_number)


garage = garage()
garage.interface()
