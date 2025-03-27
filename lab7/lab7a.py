class Time:
    def __init__(self, hour, minute, second):
        # Ensure that inputs are integers
        if not all(isinstance(i, int) for i in [hour, minute, second]):
            raise TypeError("Hour, minute, and second must be integers")

        # Time object with hour, minute, and second attributes
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    # Format time object into HH:MM:SS
    return f"{t.hour:02}:{t.minute:02}:{t.second:02}"

def sum_times(t1, t2):
    # Add two time objects and return the total
    sum = Time(0, 0, 0)
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    
    # Carry over seconds to minutes
    if sum.second >= 60:
        sum.minute += sum.second // 60
        sum.second %= 60
    
    # Carry over minutes to hours
    if sum.minute >= 60:
        sum.hour += sum.minute // 60
        sum.minute %= 60
    
    return sum

def change_time(time, seconds):
    # Modify a time object by adding seconds to it
    time.second += seconds
    
    # Carry over seconds to minutes
    if time.second >= 60:
        time.minute += time.second // 60
        time.second %= 60
    
    # Carry over minutes to hours
    if time.minute >= 60:
        time.hour += time.minute // 60
        time.minute %= 60
