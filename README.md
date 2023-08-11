# ETF Web Scraper

This project is a CLI program that scrapes ETF data from [stockanalysis.com](https://stockanalysis.com/).

## Overview

The user provides an ETF ticker and an investment amount. The program then fetches the individual holdings of the specified ETF and 
calculates the value of each holding based on the user's investment amount. The results are displayed, showing the individual stock holdings inside that ETF.

## How it Works

1. The user is prompted to enter an ETF ticker.
2. The program sends a request to stockanalysis.com to fetch the ETF's holdings.
3. The user is then prompted to enter an investment amount.
4. Based on the provided amount and the percentage of each holding in the ETF, the program calculates the value of each holding.
5. The results are displayed to the user, showing the name of the stock, its percentage in the ETF, and the calculated value based on the user's investment.

## Usage

Run the `src.py` script and follow the on-screen prompts.

## Dependencies

- BeautifulSoup
- requests
