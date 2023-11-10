#creates and writes events to a CSV file for an HTML calendar
import csv

def create_event_csv(events, csv_filename):
    # Write header to the CSV file
    header = ["Event Title", "Date", "Time", "Location"]
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(header)

        # Write events to the CSV file
        for event in events:
            csv_writer.writerow([event["title"], event["date"], event["time"], event["location"]])


# Example events
events_list = [
        {"title": "Meeting 1", "date": "2023-11-10", "time": "10:00 AM", "location": "Conference Room 1"},
        {"title": "Conference Call", "date": "2023-11-12", "time": "02:30 PM", "location": "Online"},
        # Add more events as needed
    ]
# Specify the CSV file name
csv_filename = "events.csv"

# Create and write events to the CSV file
create_event_csv(events_list, csv_filename)

print(f"Events have been written to {csv_filename}.")
