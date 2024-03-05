# Time Calculator

This Python script defines a function, `add_time`, that adds a duration of time to a start time and optionally adjusts the time based on the day of the week. It's designed to handle edge cases like transitioning from AM to PM, crossing into the next day, and adjusting through multiple days, including the calculation of the correct day of the week if specified.

## Features

- Adds a specified duration (hours and minutes) to a given start time (in 12-hour format).
- Handles transition from AM to PM and vice versa.
- Calculates and adds the day of the week if the initial day is provided.
- Accounts for days passed, indicating if the time crosses into the next day or several days later.

## How to Use

1. Call the `add_time` function with the start time, duration, and optionally, the day of the week.
2. The function returns the new time with the correct format, including the day of the week if provided, and a note on the number of days passed if applicable.

## Examples

Here are some examples of how to call the `add_time` function:

```python
print(add_time("3:00 PM", "3:10"))
# Output: 6:10 PM

print(add_time("11:30 AM", "2:32", "Monday"))
# Output: 2:02 PM, Monday

print(add_time("11:43 AM", "00:20"))
# Output: 12:03 PM

print(add_time("10:10 PM", "3:30"))
# Output: 1:40 AM (next day)

print(add_time("11:43 PM", "24:20", "tuesday"))
# Output: 12:03 AM, Thursday (2 days later)
