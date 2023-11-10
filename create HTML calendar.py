import pandas as pd
from flask import Flask, render_template_string

app = Flask(__name__)

# Read events from CSV file
def read_events_from_csv(file_path):
    df = pd.read_csv(file_path)
    return df

# Create HTML calendar
def create_html_calendar(events):
    # Replace this template with your HTML calendar template
    html_template = """
    <html>
    <head>
        <title>Event Calendar</title>
    </head>
    <body>
        <h1>Event Calendar</h1>
        <table border="1">
            <tr>
                <th>Sunday</th>
                <th>Monday</th>
                <th>Tuesday</th>
                <th>Wednesday</th>
                <th>Thursday</th>
                <th>Friday</th>
                <th>Saturday</th>
            </tr>
            {% for week in calendar %}
                <tr>
                    {% for day, events_in_day in week %}
                        <td>
                            <strong>{{ day }}</strong><br>
                            {% for event in events_in_day %}
                                {{ event }}<br>
                            {% endfor %}
                        </td>
                    {% endfor %}
                </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    """

    return render_template_string(html_template, calendar=events)

# Generate calendar with events
def generate_calendar(events):
    cal = []

    for year in range(2023, 2024):
        for month in range(1, 13):
            month_calendar = calendar.monthcalendar(year, month)
            month_events = []

            for week in month_calendar:
                week_events = []
                for day in week:
                    if day == 0:
                        week_events.append((day, []))
                    else:
                        day_events = events[(events['Year'] == year) & (events['Month'] == month) & (events['Day'] == day)]['Event'].tolist()
                        week_events.append((day, day_events))
                month_events.append(week_events)

            cal.append(month_events)

    return cal

@app.route('/')
def index():
    events = read_events_from_csv('events.csv')
    calendar_data = generate_calendar(events)
    return create_html_calendar(calendar_data)

app.run(debug=True)
