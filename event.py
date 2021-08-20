class Event:
    def __init__(self, event_id: str, title: str, type: str, start_date_time: str, image_path: str, city: str,
                 address: str, latitude, longitude, likes: int):
        self.event_id = event_id
        self.title = title
        self.type = type
        self.start_date_time = start_date_time
        self.image_path = image_path
        self.city = city
        self.address = address
        self.latitude = latitude
        self.longitude = longitude
        self.likes = likes
