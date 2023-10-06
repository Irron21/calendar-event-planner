from datetime import datetime
import re
import json
from tabulate import tabulate


class Calendar:
    def __init__(self):
        self._events = {}
        self.data = "calendar_data.json"

    def save_data(self):
            with open(self.data, "w") as file:
                json.dump(self._events, file)

    def load_data(self):
        try:
            with open(self.data, "r") as file:
                file_content = file.read()
                if file_content:
                    self._events = json.loads(file_content)
                else:
                    self._events = {}
        except FileNotFoundError:
            self._events = {}

    def add(self, date: str, event: str) -> str:
        if date in self._events:
            self._events[date].append(event)
            return f"\nAdded to the calendar {date}: {event}"
        self._events[date] = [event]
        return f"\nAdded to the calendar {date}: {event}"

    @property
    def events(self) -> dict:
        return self._events

    def edit_event(self, date: str, event: str, i: int, edit_event) -> str:
            while True:
                edit_event = edit_event.strip()
                if not edit_event:
                    print("Event cannot be empty or contain only whitespaces.")
                    edit_event = input("Please enter a valid event: ").strip()
                else:
                    break
            self._events[date][i] = edit_event
            return f"\nSuccessfully edited {event} on {date}"

    def delete(self, date: str, event: str) -> str:
            while True:
                dec = input(f"Are you sure that you want to delete {event} on {date}? ")
                yes = re.search(r"^y(?:es)?$", dec, re.IGNORECASE)
                no = re.search(r"^n(?:o)?$", dec, re.IGNORECASE)
                if no:
                    return
                elif yes:
                    self._events[date].remove(event)
                    if not self._events[date]:
                            del self._events[date]
                            print(f"\nSuccessfully deleted all the task with the date {date}.")
                            break
                    print(f"\nSuccessfully deleted {event} within the date {date}.")
                    break
                else:
                    return


calendar = Calendar()
def main():
    calendar.load_data()
    while True:
        choice = get_choice()
        print()
        if choice == 1:
            a_date, a_event = add_event()
            print(calendar.add(a_date, a_event))
        elif choice == 2:
            date = get_valid_date_input("Date to edit an event (YYYY-MM-DD): ")
            print(calendar.edit_event(date, *get_event(date), input("Edit: ")))
        elif choice == 3:
            for key, value in calendar.events.items():
                print(f"{key}: ", end="")
                print(*value, sep=", ")
        elif choice == 4:
            date = get_valid_date_input("Date to delete an event (YYYY-MM-DD): ")
            event, _ = get_event(date)
            calendar.delete(date, event)
        elif choice == 5:
            print("Bye!")
            break
    calendar.save_data()

def get_choice() -> int:
    print("""
======================
Calendar/Event Planner
======================
1 - Add event
2 - Edit event
3 - View events
4 - Delete date/event
5 - Exit planner
----------------------\n""")
    while True:
        try:
            choice = int(input("Input choice: "))
            if 1 > choice or choice > 5:
                print("Input should be a number within the choices above.")
                continue
            break
        except ValueError:
                print("Input should be a number within the choices above.")
    return choice

def get_valid_date_input(prompt):
    while True:
        date_str = input(prompt)
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            if date_str not in calendar.events:
                print(f"{date_str} does not have ant events yet.")
                continue
            return date_str
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD format.")

def add_event():
    while True:
        add_date = input("Date to add an event (YYYY-MM-DD): ")
        try:
            datetime.strptime(add_date, "%Y-%m-%d")
            while True:
                event = input(f"Event to add on {add_date}: ").strip()
                if not event:
                    print("Please enter an event")
                    continue
                return add_date, event
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD format.")
            continue


def get_event(date):
    while True:
        events_on_date = [i for i in calendar.events[date]]
        events_on_date_dict = {j+1:event for (j, event) in enumerate(events_on_date)}
        for n, events in events_on_date_dict.items():
            print(n, events, sep="|")
        try:
            n = int(input("Choice: "))
            if n not in events_on_date_dict:
                print("\nPlease choose only of the choices below.\n")
                continue
            return events_on_date_dict[n], n-1
        except ValueError:
            print("\nInput is not in any of the choices below.\n")
            continue

if __name__ == '__main__':
    main()
