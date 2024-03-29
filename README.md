# Backtest the EMA Cross Strategy for a Stock

Returns the total returns in percentage when the stock is bought and sold according to contrasted long-term and short term exponential moving average (EMA).

## Usage

Gets a candlestick chart for a stock between a period of time.

Positional Arguments:  
- stock-ticker  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                     stock ticker symbol  
- start-year     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     start year  
- start-month  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       start month  
- start-day       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       start day  

Options:
-  -h, --help       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      show this help message and exit  
-  -e Y M D, --end Y M D   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  plots chart till this date
-  -tn, --till_now    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    shows plot till now


#### Usage: ```main.py [-h] (-e YEAR MONTH DATE | -tn) stock-ticker start-year start-month start-day```

### Examples
- ```backtest.py GOOG 2009 01 01 -tn``` - return you will make till now if you started the strategy on Alphabet stock on the first day of 2009.
- ```backtest.py AAPL 2009 01 01 -e 2018 12 14``` - return you will make till 14/12/2018 if you started the strategy on Apple stock on the first day of 2009.

## Acknowledgement

Based on Richard Moglen's tutorial on [How To Back-Test Strategies](https://youtu.be/eYK2SNygAog).


