import os
import time
from datetime import datetime

import pyfiglet


def clear_terminal ():
	if os.name == "nt":
		os.system ("cls")
	else:
		os.system ("clear")
	print (pyfiglet.figlet_format ("\nPARKING    LOT"))


def user_answer ():
	while True:
		try:
			answer = int (
				input (
					"Select an option to continue:\n"
					"[1] Grab a ticket\n"
					"[2] Pay ticket\n"
					"[0] Exit\n"
				)
			)
			if answer == 0:
				print ("Thank you for your visit!")
				break
			if 1 <= answer <= 3:
				return answer
			else:
				print ("Invalid option. Please select a number between 1 and 3.")
		except ValueError:
			print ("Invalid input. Please enter a valid number.")


class garage:
	def __init__ (self):
		self.available_tickets = [num for num in range (1, 11)]
		self.ticket_records = {}  # Dictionary to store ticket issuance date and time
	
	def issue_ticket (self):
		if self.available_tickets:
			ticket_number = self.available_tickets.pop (0)
			now = datetime.now ()  # Get the current date and time
			self.ticket_records [ticket_number] = now  # Store the issuance date and time
			return ticket_number
		else:
			return None
	
	def return_ticket (self, ticket_number):
		if 1 <= ticket_number <= 10:
			self.available_tickets.append (ticket_number)
			del self.ticket_records [ticket_number]
	
	def interface (self):
		while True:
			clear_terminal ()
			print (f"Parking available: ", len (self.available_tickets), "\n")
			break


garage = garage ()
garage.interface ()
