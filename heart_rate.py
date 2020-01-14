import statistics
import math

def format_data(inp):
    '''
    Returns a dictionary of data.
    Return format: {"YYYY-MM-DD": [(HH:MM, HR), ...]}
    '''
    res = {}
    for line in inp:
        date, time, heart_rate = line.rstrip().split(",")
        if date in res:
            res[date].append((time, int(heart_rate)))
        else:
            res[date] = [(time, int(heart_rate))]

    return res


def get_hr_on_date(data, date):
    '''
    Returns a list of all heart rate measurements for the given date.
    Date format: yyyy-mm-dd
    '''
    return data[date]


def minimum_hr(heart_rates):
    '''
    Returns the minimum heart rate.
    Input format: [("hh:mm", hr),("hh:mm", hr), ...]
    '''
    return min(heart_rates, key = lambda x: x[1])[1]


def maximum_hr(heart_rates):
    '''
    Returns the maximum heart rate.
    Input format: [("hh:mm", hr),("hh:mm", hr), ...]
    '''
    return max(heart_rates, key = lambda x: x[1])[1]


def average_hr(heart_rates):
    '''
    Returns the average heart rate.
    Input format: [("hh:mm", hr),("hh:mm", hr), ...]
    '''
    return math.floor(statistics.fmean([x[1] for x in heart_rates]))
