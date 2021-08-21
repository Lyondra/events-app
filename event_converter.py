from event import Event


# event converter function that turns dictionary coming from ticketmaster api into an instance of Event class


class EventConverter:
    def __init__(self, default_likes):
        # any settings useful for the converter can be put here, such as date format to be read if relevant
        self.default_likes = default_likes

    # convert TM event (in dictionary form) to our event class: example event format is in
    # event_search_response_example.json file
    def ticketmaster_event_to_app_event(self, ticketmaster_event_dict):
        event_id = ticketmaster_event_dict["id"]
        title = ticketmaster_event_dict["name"]

        # Event type/classification
        classification1 = ticketmaster_event_dict["classifications"][0]
        event_type = classification1["segment"]["name"]

        # images
        image1 = ticketmaster_event_dict["images"][0]
        image_path = image1["url"]

        # date field
        # might be better to convert to datetime instead, so that we can use better UI formats
        event_start = ticketmaster_event_dict["dates"]["start"]
        date = "" + event_start["localDate"] + " " + (event_start["localTime"] if "localTime" in event_start else "")

        # Address/coordinates fields
        venue1 = ticketmaster_event_dict["_embedded"]["venues"][0]
        city = venue1["city"]["name"]
        address = venue1["name"] + ", " + venue1["address"]["line1"] + ", " + venue1["postalCode"]
        latitude = venue1["location"]["latitude"]
        longitude = venue1["location"]["longitude"]

        likes = self.default_likes  # will be overriden by DB

        event = Event(event_id, title, event_type, date, image_path, city, address, latitude, longitude, likes)
        return event

    # TODO unit test for this method using the sample json file content
