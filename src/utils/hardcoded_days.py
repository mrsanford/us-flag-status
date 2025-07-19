from datetime import date
from typing import List, Dict, Union
from date_helpers import get_nth_weekday, get_last_weekday

# Type alias for event structure
Event = Dict[str, Union[str, date]]


def memorial_day_event(year: int) -> Event:
    d = get_last_weekday(year, 5, 0)  # Last Monday of May
    return {
        "start_date": str(d),
        "end_date": str(d),
        "location": "National",
        "reason": "Memorial Day (until noon)",
        "name": "Memorial Day",
    }


def mlk_day_event(year: int) -> Event:
    d = get_nth_weekday(year, 1, 0, 3)
    return {
        "start_date": str(d),
        "end_date": str(d),
        "location": "National",
        "reason": "In honor of Martin Luther King Jr.",
        "name": "Martin Luther King Jr. Day",
    }


def generate_floating_halfstaff_days(year: int) -> List[Event]:
    """
    Generate recurring floating-date half-staff holidays for a given year.
    """
    return [
        mlk_day_event(year),
        memorial_day_event(year),
        {
            "start_date": f"{year}-05-15",
            "end_date": f"{year}-05-15",
            "location": "National",
            "reason": "Peace Officers Memorial Day",
            "name": "Peace Officers Memorial Day",
        },
        {
            "start_date": f"{year}-09-11",
            "end_date": f"{year}-09-11",
            "location": "National",
            "reason": "In honor of the victims of the 9/11 attacks",
            "name": "Patriot Day",
        },
        {
            "start_date": f"{year}-12-07",
            "end_date": f"{year}-12-07",
            "location": "National",
            "reason": "In honor of the lives lost at Pearl Harbor",
            "name": "Pearl Harbor Remembrance Day",
        },
    ]
