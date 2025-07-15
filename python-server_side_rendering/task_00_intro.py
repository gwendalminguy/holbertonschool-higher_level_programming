"""
Module containing function generate_invitations.
"""
import sys


def generate_invitations(template, attendees):
    """
    Function generating invitations using template.
    """
    if not isinstance(template, str):
        print("Template must be a string.")
        sys.exit()
    elif not isinstance(attendees, list):
        print("Attendees must be a list.")
        sys.exit()

    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Attendees elements must be dictionaries.")
            sys.exit()

    if len(template) == 0:
        print("Template is empty, no output files generated.")
        sys.exit()
    elif len(attendees) == 0:
        print("No data provided, no output files generated.")
        sys.exit()

    keys = ["name", "event_title", "event_date", "event_location"]

    for i in range(len(attendees)):
        new = template
        for key in keys:
            try:
                new = new.replace("{" + f"{key}" + "}", attendees[i][f"{key}"])
            except TypeError:
                new = new.replace("{" + f"{key}" + "}", "N/A")

        with open('output_{}.txt'.format(i + 1), 'w') as file:
            file.write(new)
