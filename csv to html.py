import pandas as pd
import calendar
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

# Read events from CSV file
def read_events_from_csv(file_path):
    events_df = pd.read_csv(file_path)
    return events_df

# Generate HTML calendar from events
def generate_html_calendar(events_df):
    # Create a dictionary to store events for each day
    events_by_day = {}

    for _, event in events_df.iterrows():
        date_str = event['Date']
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        day_key = date_obj.strftime('%Y-%m-%d')

        if day_key not in events_by_day:
            events_by_day[day_key] = []

        events_by_day[day_key].append({
            'title': event['Event Title'],
            'time': event['Time'],
            'location': event['Location']
        })

    # Load Jinja2 template
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('calendar_template.html')

    # Generate HTML using the template
    html_output = template.render(events_by_day=events_by_day)

    return html_output

# Save HTML to a file
def save_html_to_file(html_content, output_file):
    with open(output_file, 'w') as file:
        file.write(html_content)

# Replace 'your_events.csv' with the path to your CSV file
events_file_path = 'events.csv'

# Read events from CSV
events_df = read_events_from_csv(events_file_path)

# Generate HTML calendar
html_calendar = generate_html_calendar(events_df)

# Replace 'output_calendar.html' with the desired output file name
output_file_path = 'output_calendar.html'

# Save HTML to a file
save_html_to_file(html_calendar, output_file_path)
