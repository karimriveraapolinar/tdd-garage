def enter_garage(garage, car_id, entry_hour):
    if len(garage['cars']) >= garage['capacity']:
        raise ValueError("Garage is full")

    garage['cars'][car_id] = entry_hour


def exit_garage(garage, car_id):
    pass


def get_available_spots(garage):
    pass


def calculate_fee(hours,rate):
    if hours <0 or rate < 0:
        raise ValueError("Hours or Rate cannot be negative ")

    return round(hours * rate, 2)