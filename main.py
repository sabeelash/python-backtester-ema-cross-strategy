import argparse
import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr

yf.pdr_override()

parser = argparse.ArgumentParser(description='Gets a candlestick chart for a stock between a period of time')

parser.add_argument('stock', metavar='stock-ticker', type=str, help='stock ticker symbol')

parser.add_argument('start_year', metavar='start-year', type=int, help='start year')
parser.add_argument('start_month', metavar='start-month', type=int, help='start month')
parser.add_argument('start_day', metavar='start-day', type=int, help='start day')

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-e', '--end', type=int, nargs=3, metavar=('YEAR', 'MONTH', 'DATE'),
                   help='plots chart till this date')
group.add_argument('-tn', '--till_now', action='store_true', help='shows plot till now')

args = parser.parse_args()

stock = args.stock
# print(stock)

startyear = args.start_year
startmonth = args.start_month
startday = args.start_day

start = dt.datetime(startyear, startmonth, startday)

till_now = args.till_now
if not till_now:
    end = args.end
    end_year = end[0]
    end_month = end[1]
    end_day = end[2]
    end = dt.datetime(end_year, end_month, end_day)
else:
    end = dt.datetime.now()

df = pdr.get_data_yahoo(stock, start, end)

emasUsed = [3, 5, 8, 10, 12, 15, 30, 35, 40, 45, 50, 60]
for x in emasUsed:
    ema = x
    df["Ema_" + str(ema)] = round(df.iloc[:, 4].ewm(span=ema, adjust=False).mean(), 2)

df = df.iloc[60:]

pos = 0
num = 0
percentchange = []

for i in df.index:
    cmin = min(df["Ema_3"][i], df["Ema_5"][i], df["Ema_8"][i], df["Ema_10"][i], df["Ema_12"][i], df["Ema_15"][i])
    cmax = max(df["Ema_30"][i], df["Ema_35"][i], df["Ema_40"][i], df["Ema_45"][i], df["Ema_50"][i], df["Ema_60"][i])

    close = df["Adj Close"][i]

    if (cmin > cmax):
        if (pos==0):
            bp = close
            pos = 1
    elif (cmin < cmax):
        if (pos == 1):
            pos = 0
            sp = close
            pc = (sp / bp - 1) * 100
            percentchange.append(pc)

    # when there is a position open at the end
    if (num == df["Adj Close"].count() - 1 and pos == 1):
        pos = 0
        sp = close
        pc = (sp / bp - 1) * 100
        percentchange.append(pc)

    num += 1

gains = 0
ng = 0
losses = 0
nl = 0
totalR = 1

for i in percentchange:
    if (i > 0):
        gains += i
        ng += 1
    else:
        losses += i
        nl += 1
    totalR = totalR * ((i / 100) + 1)

totalR = round((totalR - 1) * 100, 2)

if (ng > 0):
    avgGain = gains / ng
    maxR = str(max(percentchange))
else:
    avgGain = 0
    maxR = "undefined"

if (nl > 0):
    avgLoss = losses / nl
    maxL = str(min(percentchange))
    ratio = str(-avgGain / avgLoss)
else:
    avgLoss = 0
    maxL = "undefined"
    ratio = "inf"

if (ng > 0 or nl > 0):
    battingAvg = ng / (ng + nl)
else:
    battingAvg = 0

print("EMAs used: " + str(emasUsed))
print("Batting Avg: " + str(battingAvg))
print("Gain/loss ratio: " + ratio)
print("Average Gain and Loss: " + str(avgGain) + " and " +str(avgLoss))
print("Max Return and Loss: " + maxR + " and " + maxL)
print("Total return over " + str(ng + nl) + " trades: " + str(totalR) + "%")