import sys
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import pandas as pd
from pandas.plotting import register_matplotlib_converters
import numpy as np

import heart_rate
import math


register_matplotlib_converters()

def main():
    #f = open(sys.argv[1])
    f = open("hr_data.csv")
    date_title, time_title, heart_rate_title = f.readline().rstrip().split(',')
    formatted_hr = heart_rate.format_data(f)
    date_to_get = "2019-12-27"
    day_hr = heart_rate.get_hr_on_date(formatted_hr, date_to_get)

    times = []
    rates = []

    for i in day_hr:
        t = datetime.datetime.strptime(i[0], '%H:%M')
        times.append(t.strftime('%H:%M'))
        rates.append(i[1])

    idx = pd.date_range("01:00", "23:51", freq = "min")
    df = pd.Series(np.random.randn(len(idx)), index = idx)

    # plot
    fig, ax = plt.subplots()
    hours = mdates.HourLocator()
    h_fmt = mdates.DateFormatter('%H')

    #ax.plot(df.index, df.values, color = "black", linewidth = 0.4)
    ax.plot(times, rates, color = "black", linewidth = 0.4)

    ax.xaxis.set_major_locator(hours)
    ax.xaxis.set_major_formatter(h_fmt)

    ax.set(xlabel=time_title, ylabel=heart_rate_title, title="Heart rate for " + date_to_get)

    fig.autofmt_xdate()

    #ax.grid()

    plt.show()

main()
