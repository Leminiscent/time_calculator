def add_time(start, duration, day=None):
    days_of_week = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    days_later = 0

    # Split the start time and duration into components
    start_time, period = start.split()
    start_hours, start_minutes = map(int, start_time.split(":"))
    duration_hours, duration_minutes = map(int, duration.split(":"))

    # Convert start time to 24-hour format
    if period == "PM":
        start_hours += 12

    # Add duration to start time
    total_hours = start_hours + duration_hours
    total_minutes = start_minutes + duration_minutes

    # Handle minutes overflow
    if total_minutes >= 60:
        total_hours += 1
        total_minutes -= 60

    # Handle hours overflow and count days passed
    days_later = total_hours // 24
    total_hours %= 24

    # Convert back to 12-hour format
    if total_hours == 0:
        total_hours = 12
        period = "AM"
    elif total_hours == 12:
        period = "PM"
    elif total_hours > 12:
        total_hours -= 12
        period = "PM"
    else:
        period = "AM"

    # Prepare the new time format
    new_time = f"{total_hours}:{str(total_minutes).zfill(2)} {period}"

    # Add the day of the week, if provided
    if day:
        day_index = (days_of_week.index(day.capitalize()) + days_later) % 7
        new_day = days_of_week[day_index]
        new_time += f", {new_day}"

    # Add notation for days later
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"

    return new_time


def main():
    print(add_time("3:00 PM", "3:10"))
    print(add_time("11:30 AM", "2:32", "Monday"))
    print(add_time("11:43 AM", "00:20"))
    print(add_time("10:10 PM", "3:30"))
    print(add_time("11:43 PM", "24:20", "tuesday"))


if __name__ == "__main__":
    main()
