import os


def generate_invitations(template, attendees):
    if not isinstance(template, str) or not isinstance(attendees, list):
        print("Error: Invalid input types.")
        return
    if not all(isinstance(attendee, dict) for attendee in attendees):
        print("Error: All attendees must be dictionaries.")
        return
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return
    for index, attendee in enumerate(attendees, start=1):
        name = attendee.get("name")
        title = attendee.get("event_title")
        date = attendee.get("event_date")
        location = attendee.get("event_location")

        name = name if name is not None else "N/A"
        title = title if title is not None else "N/A"
        date = date if date is not None else "N/A"
        location = location if location is not None else "N/A"

        personalized = template.replace("{name}", name)
        personalized = personalized.replace("{event_title}", title)
        personalized = personalized.replace("{event_date}", date)
        personalized = personalized.replace("{event_location}", location)

        filename = f"output_{index}.txt"

        try:
            with open(filename, "w", encoding="utf-8") as file:
                file.write(personalized)
        except Exception as e:
            print(f"Error writing to file {filename}: {e}")
