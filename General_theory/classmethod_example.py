class Event:
    def __init__(self, description, event_date):
        self.description = description
        self.date = event_date

    def __str__(self):
        return f"Event \"{self.description}\" at {self.date}"

    @classmethod
    def from_string(cls, user_input):
        description = extract_description(user_input)
        date = extract_date(user_input)
        return cls(description, date)


def extract_description(user_string):
    """заглушка для простоты"""
    return "Открытие конференции"


def extract_date(user_string):
    """заглушка для простоты"""
    return 2022, 11, 1


event = Event.from_string("добавить в мой календарь открытие чемпионата мира по футболу на 14 июня 2018 года")
print(event)
