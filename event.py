


class Event:
    def __init__(self, event_id, title: str, type: str, budget: str, city: str, address: str, image_path: str,
                 datetime, likes: int, description: str):
        self.event_id = event_id
        self.title = title
        self.type = type
        self.budget = budget
        self.city = city
        self.address = address
        self.image_path = image_path
        self.datetime = datetime
        self.likes = likes
        self.description = description
