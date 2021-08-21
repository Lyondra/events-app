from flask import Flask, render_template, request
from datetime import datetime, date, timedelta
import requests, json
from event import Event
from event_converter import EventConverter

# from requests.exceptions import HTTPError # Potentially TODO


app = Flask(__name__)

# Some mock events to progress with UI work till we have the actual live events data from the Ticketmaster API
mock_events = [
    Event("a564fa", "Mama Mia!", "Arts & Theater", "2021-10-14 19:00:00", "./static/placeholder.png", "London",
          "SE1 1AA", 51.5, -0.1, 2),
    Event("h5hg74", "Les Misérables", "Arts & Theater", "2021-10-14 19:00:00", "./static/placeholder.png",
          "London", "SE1 2AA", 51.5, -0.1, 2),
    Event("uyy998", "The Phantom of the Opera", "Arts & Theater", "2021-10-14 19:00:00",
          "./static/placeholder.png", "London", "SE1 3AA", 51.5, -0.1, 2),
    Event("t8999r", "U2", "Music", "2021-10-14 19:00:00", "./static/placeholder.png", "London", "SE1 4AA",
          51.5, -0.1, 2),
    Event("cv3cd9", "Metallica", "Music", "2021-10-14 19:00:00", "./static/placeholder.png", "London",
          "SE1 5AA", 51.5, -0.1, 2),
    Event("712dfd", "The Curious Incident of the Dog in the Nighttime", "Arts & Theater",
          "2021-10-14 19:00:00", "./static/placeholder.png", "London", "SE6 1AA", 51.5, -0.1, 2),
]

TICKETMASTER_API_EVENTDISCOVERY_URL = "https://app.ticketmaster.com/discovery/v2/events?apikey=7elxdku9GGG5k8j0Xm8KWdANDgecHMV0&locale=*"

SEGMENT_NAMES_TO_SEGMENT_IDS = {
    'Arts & Theatre': 'KZFzniwnSyZfZ7v7na',
    'Film': 'KZFzniwnSyZfZ7v7nn',
    'Music': 'KZFzniwnSyZfZ7v7nJ',
    'Miscellaneous': 'KZFzniwnSyZfZ7v7n1',
    'Sports': 'KZFzniwnSyZfZ7v7nE'
}


@app.route("/")
def main_page():
    return render_template('search.html')


@app.route("/results")
def results_page():
    type = request.args.get('type')
    city = request.args.get('city')
    days = int(request.args.get('days'))
    mock = request.args.get('mock')  # add mock=1 to url to use mock data

    # get events based on the specs above, either from the mock content or from a call to Ticketmaster discovery API
    if mock == "1":
        events = search_mock_events(type, city)  # date not added
    else:
        url = build_searchevents_url(type, city, datetime.now(), days)
        events = perform_event_ticketmaster_api_call(url)

    count = len(events)
    return render_template('results.html', type=type, city=city, days=days, events=events, count=count, mock=mock)


@app.route("/details")
def details_page():
    event_id = request.args.get('event_id')  # saves the event_id from the url to a variable
    mock = request.args.get('mock')
    if mock == "1":
        event = retrieve_mock_event(event_id)
    else:
        url = build_singleeventretrieval_url(event_id)
        event = perform_event_ticketmaster_api_call(url)[0]
    # includes the number of likes from the DB in the event record
    # TODO
    return render_template('details.html', event=event, mock=mock)  # pass full event object to flask template engine


@app.route("/api/event/<string:event_id>/like", methods=['PATCH'])
def api_endpoint_event_like(event_id):
    # TODO
    return '', 204  #no content http status code



def perform_event_ticketmaster_api_call(url):
    print(url)
    response = requests.get(url)
    # print(response)
    if response.status_code != 200:
        raise ValueError("API returned error " + str(response.status_code))
    data = json.loads(response.text)
    # print(data)
    if "_embedded" not in data:
        return []  # no results
    raw_events = data["_embedded"]["events"]
    events = []
    event_converter = EventConverter(0)
    for raw_event in raw_events:
        event = event_converter.ticketmaster_event_to_app_event(raw_event)
        events.append(event)
    return events


def build_searchevents_url(event_type, city, start_datetime, number_of_days):
    # prepare the date range
    start_date = start_datetime.date()
    end_date = start_date + timedelta(days=(number_of_days - 1))  # add number of days to get end of the time range
    end_datetime = datetime.combine(end_date, datetime.max.time())  # creates datetime (takes the end of day - 23:59:59)
    start_datetime_iso = start_datetime.replace(microsecond=0).isoformat() + "Z"
    end_datetime_iso = end_datetime.replace(microsecond=0).isoformat() + "Z"
    # build the url with the relevant query parameters
    url = TICKETMASTER_API_EVENTDISCOVERY_URL + "&size=100&countryCode=GB"  # just n events, no pagination.
    url += "&city=" + city
    url += "&segmentId=" + SEGMENT_NAMES_TO_SEGMENT_IDS[event_type]
    url += "&startDateTime=" + start_datetime_iso
    url += "&endDateTime=" + end_datetime_iso
    return url


def build_singleeventretrieval_url(event_id):
    return TICKETMASTER_API_EVENTDISCOVERY_URL + "&id=" + event_id


def search_mock_events(type, city):
    events = mock_events
    events = list(filter(lambda obj: obj.type == type, events))
    events = list(filter(lambda obj: obj.city == city, events))
    return events


def retrieve_mock_event(event_id):
    events = mock_events
    event_id = list(filter(lambda obj: obj.event_id == event_id, events))[0]
    return event_id


app.run(debug=True)
