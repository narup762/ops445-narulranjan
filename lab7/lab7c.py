# Define the Time class
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

# Function to format time as a string
def format_time(time):
    return f"{time.hour:02}:{time.minute:02}:{time.second:02}"

# Function to add two Time objects
def sum_times(t1, t2):
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_seconds)

# Function to modify a Time object by a given number of seconds
def change_time(time, seconds):
    total_seconds = time_to_sec(time) + seconds
    while total_seconds < 0:
        total_seconds += 86400  # Adjust for negative values (wrap around)
    new_time = sec_to_time(total_seconds % 86400)
    time.hour, time.minute, time.second = new_time.hour, new_time.minute, new_time.second

# Convert Time object to total seconds from midnight
def time_to_sec(time):
    minutes = time.hour * 60 + time.minute
    return minutes * 60 + time.second

# Convert total seconds from midnight to Time object
def sec_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
