from bs4 import BeautifulSoup
import requests

retry = True
while (retry):

    while True:
        etfTicker = input('ticker: ')
        url = 'https://stockanalysis.com/etf/' + etfTicker + '/holdings/'
        try:
            html = requests.get(url)
            
            if html.status_code == 200: # good request exit while loop
                break
            else:
                print("Invalid ticker. Please try again.")
        except requests.exceptions.RequestException as e:
            print("Error occurred:", e)
            print("Invalid ticker. Please try again.") 

    while True:
        try:
            value = int(input('Enter an integer value: '))
            break  # Exit the loop if a valid integer is entered
        except ValueError:
            print("Invalid input. Please enter an integer.")

    holdings = {}

    soup = BeautifulSoup(html.content, 'html.parser')

    table_rows = soup.select('#main > div > div > div > div > div.table-wrap > table > tbody > tr') # url path to reach datatable on stockanalysis.com

    for row in table_rows:
        cells = row.select('td')
        if len(cells) >= 4: # ensure we are only pulling data for etf row data and not any excess data is scraped
            stock_name = cells[1].text.strip() 
            percent = cells[3].text.strip('%')
            tickerValue = "%.2f" % (value*(float(percent)/100)) # format and calculate value derived from user investment
            holdings[stock_name] = str(percent) + '% : $' + str(tickerValue) # format map
    while True:
        try:
            total_holdings = len(holdings)
            show_size = int(input(f"How many holdings would you like to show? There are {total_holdings} in total: "))
            if show_size <= total_holdings: 
                break  
            else:
                print("Invalid input. The number of holdings to show cannot exceed the total number of holdings.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")    
    count = 0
    for stock_name, value in holdings.items():
        if count < int(show_size): # show stocks that are in the top holdings of the etf filtered by user choice
            print(stock_name + ' : ' + value)
            count += 1
        else:
            break

    while True:
        searchAgain = input('Would you like to search for another etf? (y/n)')
        searchAgain.lower() # UX if user enters Y or N 
        if(searchAgain == 'y' or 'n'):
            if(searchAgain == 'y'):
                retry = True
                del holdings #erase previous data 
                break
            else:
                retry = False
                break
