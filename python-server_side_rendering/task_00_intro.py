"""
Module containing function generate_invitations.
"""
import sys


def generate_invitations(template, attendees):
    """
    Function generating invitations using template.
    """
    if not isinstance(template, str):
        raise TypeError("Template must be a string.")
    elif not isinstance(attendees, list):
        raise TypeError("Attendees must be a list.")

    for attendee in attendees:
        if not isinstance(attendee, dict):
            raise TypeError("Attendees elements must be dictionaries.")

    if len(template) == 0:
        raise ValueError("Template is empty, no output files generated.")
    elif len(attendees) == 0:
        raise ValueError("No data provided, no output files generated.")

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
