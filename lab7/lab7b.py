#!/usr/bin/env python3

class Time:
    def __init__(self, hour, minute, second):
        if not all(isinstance(i, int) for i in [hour, minute, second]):
            raise TypeError("Hour, minute, and second must be integers")
        self.hour = hour
        self.minute = minute
        self.second = second

# Function to format time object as HH:MM:SS
def format_time(time):
    return f"{time.hour:02}:{time.minute:02}:{time.second:02}"

# Function to check if time is valid
def valid_time(time):
    return 0 <= time.hour and 0 <= time.minute < 60 and 0 <= time.second < 60

# Function to sum two time objects
def sum_times(t1, t2):
    sum_time = Time(t1.hour + t2.hour, t1.minute + t2.minute, t1.second + t2.second)
    
    while sum_time.second >= 60:
        sum_time.second -= 60
        sum_time.minute += 1
    while sum_time.minute >= 60:
        sum_time.minute -= 60
        sum_time.hour += 1
    
    return sum_time

# Function to change time by a given number of seconds
def change_time(time, seconds):
    time.second += seconds
    
    # Carry over for positive values
    while time.second >= 60:
        time.second -= 60
        time.minute += 1
    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1
    
    # Borrow for negative values
    while time.second < 0:
        time.second += 60
        time.minute -= 1
    while time.minute < 0:
        time.minute += 60
        time.hour -= 1
    
    return None