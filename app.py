from flask import Flask, render_template, request
from event import Event
from datetime import datetime

app = Flask(__name__)

# Some mock events to progress with UI work till we have the actual live events data from the Ticketmaster API
mock_events = [
    Event("a564fa", "Mama Mia!", "musical", "average", "London", "SE1 1AA", "./static/placeholder.png",
          datetime.strptime("21 June, 2021", "%d %B, %Y"), 2, "blah blah blah blah blah blah blah blah blah "),
    Event("h5hg74", "Les Misérables", "musical", "average", "London", "N1 2FT", "./static/placeholder.png",
          datetime.strptime("21 June, 2021", "%d %B, %Y"), 2, "blah blah blah blah blah blah blah blah blah "),
    Event("uyy998", "The Phantom of the Opera", "musical", "high", "London", "EC1 0ER", "./static/placeholder.png",
          datetime.strptime("21 June, 2021", "%d %B, %Y"), 2, "blah blah blah blah blah blah blah blah blah "),
    Event("t8999r", "U2", "concert", "high", "London", "SE1 8AA", "./static/placeholder.png",
          datetime.strptime("21 June, 2021", "%d %B, %Y"), 3, "blah blah blah blah blah blah blah blah blah "),
    Event("cv3cd9", "Metallica", "concert", "average", "London", "N1 5FT", "./static/placeholder.png",
          datetime.strptime("21 June, 2021", "%d %B, %Y"), 5, "blah blah blah blah blah blah blah blah blah "),
    Event("712dfd", "The Curious Incident of the Dog in the Nighttime", "theatre", "average", "London", "EC1 9ER",
          "./static/placeholder.png", datetime.strptime("21 June, 2021", "%d %B, %Y"), 2,
          "blah blah blah blah blah blah blah blah blah "),
]


@app.route("/")
def main_page():
    return render_template('search.html')


@app.route("/results")
def results_page():
    type = request.args.get('type')
    city = request.args.get('city')
    budget = request.args.get('budget')

    events = get_events_by_type_city_budget(type, city, budget)
    count = len(events)
    return render_template('results.html', type=type, city=city, budget=budget, events=events, count=count)


def get_events_by_type_city_budget(type, city, budget):
    events = mock_events
    if type != 'all':
        events = list(filter(lambda obj: obj.type == type, events))
    if city != 'all':
        events = list(filter(lambda obj: obj.city == city, events))
    if budget != 'all':
        events = list(filter(lambda obj: obj.budget == budget, events))
    return events


app.run(debug=True)
