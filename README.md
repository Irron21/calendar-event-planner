
# Calendar/Event Planner

This is a simple command-line calendar and event planner program, developed as the final project for CS50P (Introdduction to Programming with Python) offered by Harvard University. It allows you to manage your events, add, edit, view, and delete them on specific dates.

## [Video Demo](https://youtu.be/hs0brxo5XFM)

## Features

- **Add Event**: You can add events to specific dates, providing a description for each event.

- **Edit Event**: You have the option to edit existing events on a selected date.

- **View Events**: You can view events in a tabular format, providing a clear overview of your schedule.

- **Delete Event**: You can delete events by specifying the date and event description.

## Usage

1. Run the program by executing the `calendar.py` script in your Python environment.

2. The program will display a menu with the following options:
    - **Add Event**: Choose this option to add a new event by specifying the date and event description.

    - **Edit Event**: Select this option to edit an existing event by specifying the date and event description.

    - **View Events**: This option displays your calendar in a tabular format, showing events for each date.

    - **Delete Event**: Use this option to delete an event by specifying the date and event description.

    - **Exit Planner**: Choose this option to exit the program.

3. Follow the on-screen prompts to perform the desired actions.

4. Your data will be saved automatically to a JSON file (`calendar_data.json`) for future use.

## Requirements

- Python 3.x
### Libraries Used
- The `tabulate` library
- The `datetime` library
- The `re` library
- The `json` library

## Author

Irron Miguel M. Panganiban

## Acknowledgments

- This project was developed as the final project for CS50P at Harvard University.
- Special thanks to the CS50P course instructors and mentors for their guidance and support.
