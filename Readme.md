# Parking Lot

### Import necessary modules:

- os - for clearing terminal screen
- time - for sleeping/pausing
- datetime - for working with dates and times
- pyfiglet - for creating ASCII art banners

### Define user_answer()

- Prints menu options and gets numeric input
- Validates input is 0-3
- Returns valid input

### Define Garage class:

- Constructor initializes available tickets and ticket records dict
- issue_ticket() issues next available ticket, stores issuance in dict, returns ticket number
- return_ticket() makes ticket available again and removes from dict
- interface() contains main logic:

    - Prints available tickets
    - Calls user_answer() to get input
    - If 1, issue ticket and print details or error
    - If 2, prompt for ticket number
    - Ask to pay
